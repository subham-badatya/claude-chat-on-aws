from anthropic import AnthropicAWS

client = AnthropicAWS(
    aws_region="ap-south-1",
    workspace_id="wrkspc_xxxx"
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello!"}
    ],
)

print(message.content[0].text)
