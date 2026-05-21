"""
Example workflows demonstrating Hybrid AI capabilities
"""

example_workflows = {
    "content_creation": {
        "description": "Create complete multimedia content from a single prompt",
        "steps": [
            {
                "action": "qwen_generate",
                "params": {
                    "prompt": "Create a detailed scene description for a sci-fi video",
                    "max_tokens": 500
                }
            },
            {
                "action": "generate_image",
                "params": {
                    "prompt": "Futuristic cyberpunk city, neon lights, flying cars, digital art",
                    "num_images": 1,
                    "height": 1024,
                    "width": 1024
                }
            },
            {
                "action": "generate_video",
                "params": {
                    "image_path": "workspace/image_*.png",
                    "num_frames": 30,
                    "num_inference_steps": 25
                }
            }
        ]
    },
    
    "data_analysis": {
        "description": "Analyze data, generate visualizations, and create reports",
        "steps": [
            {
                "action": "execute_code",
                "params": {
                    "code": """
import json
import numpy as np

# Generate sample data
data = {
    "months": ["Jan", "Feb", "Mar", "Apr", "May"],
    "values": np.random.randint(10, 100, 5).tolist()
}

print("Data Analysis Results:")
print(json.dumps(data, indent=2))
print(f"Average: {np.mean(data['values']):.2f}")
print(f"Max: {max(data['values'])}")
print(f"Min: {min(data['values'])}")
""",
                    "description": "Analyze and process data"
                }
            },
            {
                "action": "qwen_generate",
                "params": {
                    "prompt": "Write a business report summary of sales data",
                    "max_tokens": 300
                }
            }
        ]
    },
    
    "research_project": {
        "description": "Research topic, gather information, generate content",
        "steps": [
            {
                "action": "web_search",
                "params": {
                    "query": "artificial intelligence breakthroughs 2024",
                    "num_results": 5
                }
            },
            {
                "action": "qwen_generate",
                "params": {
                    "prompt": "Summarize the latest AI breakthroughs and their implications",
                    "max_tokens": 400
                }
            },
            {
                "action": "generate_image",
                "params": {
                    "prompt": "Illustration of AI neural networks and machine learning",
                    "num_images": 1
                }
            }
        ]
    },
    
    "creative_storytelling": {
        "description": "Generate story, create visuals, produce video",
        "steps": [
            {
                "action": "qwen_generate",
                "params": {
                    "prompt": "Write a short creative story about time travel, max 200 words",
                    "max_tokens": 300
                }
            },
            {
                "action": "generate_image",
                "params": {
                    "prompt": "A person standing in front of a time machine, sci-fi aesthetic",
                    "num_images": 2
                }
            },
            {
                "action": "generate_video",
                "params": {
                    "image_path": "workspace/image_*.png",
                    "num_frames": 20,
                    "num_inference_steps": 20
                }
            }
        ]
    },
    
    "code_development": {
        "description": "Generate code, test it, improve based on results",
        "steps": [
            {
                "action": "qwen_generate",
                "params": {
                    "prompt": "Generate Python code to calculate Fibonacci sequence up to 10 numbers",
                    "max_tokens": 200
                }
            },
            {
                "action": "execute_code",
                "params": {
                    "code": """
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print("Fibonacci Sequence:")
print(fibonacci(10))
""",
                    "description": "Test Fibonacci implementation"
                }
            }
        ]
    },
    
    "marketing_campaign": {
        "description": "Create marketing content: copy, images, and video",
        "steps": [
            {
                "action": "qwen_generate",
                "params": {
                    "prompt": "Write compelling marketing copy for a premium tech product",
                    "max_tokens": 300
                }
            },
            {
                "action": "generate_image",
                "params": {
                    "prompt": "Professional product photo, modern tech gadget, clean background",
                    "num_images": 2
                }
            },
            {
                "action": "generate_video",
                "params": {
                    "image_path": "workspace/image_*.png",
                    "num_frames": 25,
                    "num_inference_steps": 25
                }
            }
        ]
    }
}


def run_example(workflow_name: str):
    """
    Run a predefined example workflow
    
    Usage:
        from examples import run_example, example_workflows
        from hybrid_workflow import HybridWorkflow
        
        workflow = HybridWorkflow()
        config = example_workflows["content_creation"]
        workflow.run_workflow(config)
    """
    if workflow_name in example_workflows:
        config = example_workflows[workflow_name]
        print(f"Running workflow: {workflow_name}")
        print(f"Description: {config['description']}")
        return config
    else:
        available = ", ".join(example_workflows.keys())
        print(f"Unknown workflow. Available: {available}")
        return None


if __name__ == "__main__":
    print("Available Example Workflows:\n")
    for name, config in example_workflows.items():
        print(f"✓ {name}")
        print(f"  {config['description']}")
        print()
