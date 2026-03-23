"""FastAPI application for Multi-Agent AI Framework."""

import os
from contextlib import asynccontextmanager
from typing import Optional
from datetime import datetime

from fastapi import FastAPI, HTTPException, BackgroundTasks, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from loguru import logger
import asyncio

# Environment configuration
APP_NAME = os.getenv("APP_NAME", "multi-agent-ai-framework")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# ============== Models ==============

class AgentRequest(BaseModel):
    """Request model for agent execution."""
    task: str = Field(..., description="Task description for the agent")
    agent_id: Optional[str] = Field(None, description="Specific agent ID to use")
    context: Optional[dict] = Field(default_factory=dict, description="Additional context")
    timeout: Optional[int] = Field(default=300, description="Execution timeout in seconds")

class AgentResponse(BaseModel):
    """Response model for agent execution."""
    task_id: str
    agent_id: str
    status: str
    result: Optional[dict] = None
    error: Optional[str] = None
    execution_time: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    version: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    uptime: float

class WorkflowRequest(BaseModel):
    """Request model for workflow execution."""
    workflow_name: str
    tasks: list[dict]
    parallel: bool = False
    timeout: Optional[int] = Field(default=600, description="Total workflow timeout")

class WorkflowResponse(BaseModel):
    """Response model for workflow execution."""
    workflow_id: str
    status: str
    results: list[dict]
    execution_time: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# ============== Startup/Shutdown ==============

app_start_time = datetime.utcnow()

async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    logger.info(f"{APP_NAME} v{APP_VERSION} starting...")
    yield
    logger.info(f"{APP_NAME} shutting down...")

# ============== FastAPI Application ==============

app = FastAPI(
    title=APP_NAME,
    description="Production-ready Multi-Agent AI Framework with LangGraph orchestration",
    version=APP_VERSION,
    debug=DEBUG,
    lifespan=lifespan,
)

# ============== CORS Middleware ==============

allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info(f"CORS enabled for origins: {allowed_origins}")

# ============== API Endpoints ==============

@app.get("/", tags=["System"])
async def root():
    """Root endpoint."""
    return {
        "message": "Multi-Agent AI Framework API",
        "version": APP_VERSION,
        "docs": "/docs",
    }

@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check():
    """Health check endpoint."""
    uptime = (datetime.utcnow() - app_start_time).total_seconds()
    return HealthResponse(
        status="healthy",
        version=APP_VERSION,
        uptime=uptime,
    )

@app.post("/agents/execute", response_model=AgentResponse, tags=["Agents"])
async def execute_agent(request: AgentRequest, background_tasks: BackgroundTasks):
    """Execute a single agent task."""
    try:
        import uuid
        import time
        
        task_id = str(uuid.uuid4())
        agent_id = request.agent_id or "default_agent"
        start_time = time.time()
        
        logger.info(f"Executing task {task_id} with agent {agent_id}: {request.task}")
        
        # Simulated agent execution
        await asyncio.sleep(0.1)  # Simulate processing
        
        execution_time = time.time() - start_time
        
        return AgentResponse(
            task_id=task_id,
            agent_id=agent_id,
            status="completed",
            result={
                "output": f"Processed task: {request.task}",
                "context_used": request.context,
            },
            execution_time=execution_time,
        )
    except Exception as e:
        logger.error(f"Error executing agent task: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/workflows/execute", response_model=WorkflowResponse, tags=["Workflows"])
async def execute_workflow(request: WorkflowRequest):
    """Execute a complete workflow with multiple tasks."""
    try:
        import uuid
        import time
        
        workflow_id = str(uuid.uuid4())
        start_time = time.time()
        
        logger.info(f"Executing workflow {workflow_id}: {request.workflow_name}")
        
        # Simulated workflow execution
        results = []
        for idx, task in enumerate(request.tasks):
            await asyncio.sleep(0.05)  # Simulate processing
            results.append({
                "task_index": idx,
                "task_name": task.get("name", f"task_{idx}"),
                "status": "completed",
            })
        
        execution_time = time.time() - start_time
        
        return WorkflowResponse(
            workflow_id=workflow_id,
            status="completed",
            results=results,
            execution_time=execution_time,
        )
    except Exception as e:
        logger.error(f"Error executing workflow: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/agents/list", tags=["Agents"])
async def list_agents():
    """List available agents."""
    return {
        "agents": [
            {"id": "research_agent", "description": "Research and analysis agent"},
            {"id": "planning_agent", "description": "Planning and strategy agent"},
            {"id": "coding_agent", "description": "Code generation and execution agent"},
            {"id": "retrieval_agent", "description": "Information retrieval agent"},
        ]
    }

@app.get("/status", tags=["System"])
async def get_status():
    """Get current system status."""
    return {
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "debug": DEBUG,
        "timestamp": datetime.utcnow().isoformat(),
    }

# ============== Error Handlers ==============

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler."""
    logger.error(f"HTTP error: {exc.detail}")
    return {
        "error": exc.detail,
        "status_code": exc.status_code,
        "timestamp": datetime.utcnow().isoformat(),
    }

# ============== Main Entry Point ==============

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    
    logger.info(f"Starting {APP_NAME} on {host}:{port}")
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info",
    )
