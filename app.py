import gradio as gr
import mlx_lm
from mlx_lm.sample_utils import make_sampler

# Load the fine-tuned model
print("Loading fine-tuned model...")
model, tokenizer = mlx_lm.load(
    'mlx-community/Llama-3.2-3B-Instruct-4bit',
    adapter_path='./models/llama3.2-3b-quotes-lora-mlx'
)
print("✅ Model loaded successfully!")

def chat_respond(message, temperature):
    """Generate chat response"""
    prompt = f"{message}"
    
    # Generate response
    sampler = make_sampler(temp=temperature)
    
    try:
        response = mlx_lm.generate(
            model, tokenizer, 
            prompt=prompt, 
            max_tokens=150, 
            sampler=sampler
        )
        
        # Clean up the response (remove the original prompt)
        if prompt in response:
            response = response.replace(prompt, "").strip()
        
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Create simple Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Motivational Quote Generator")
    
    with gr.Row():
        temperature = gr.Slider(0.1, 1.5, 0.7, label="Temperature")
    
    with gr.Row():
        with gr.Column():
            prompt_input = gr.Textbox(
                label="Your Prompt",
                placeholder="Give me advice about courage",
                lines=2
            )
            
            generate_btn = gr.Button("Generate", variant="primary")
            
            response_output = gr.Textbox(
                label="Response",
                lines=6,
                interactive=False
            )
    
    # Examples
    gr.Examples(
        examples=[
            "Give me advice about perseverance",
            "Give me advice about courage", 
            "Give me advice about success",
            "Give me advice about self-discipline"
        ],
        inputs=prompt_input
    )
    
    # Event handlers
    generate_btn.click(
        fn=chat_respond,
        inputs=[prompt_input, temperature],
        outputs=response_output
    )
    
    prompt_input.submit(
        fn=chat_respond,
        inputs=[prompt_input, temperature],
        outputs=response_output
    )

# Launch interface
if __name__ == "__main__":
    demo.launch()