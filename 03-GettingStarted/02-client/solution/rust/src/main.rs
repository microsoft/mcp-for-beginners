use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "server" in the same directory
    let workspace_root = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).parent();

    let server_dir = match workspace_root {
        Some(root) => root.join("server"),
        None => {
            eprintln!("Error: Failed to locate workspace root");
            return Ok(()); // or return an appropriate error
        }
    };

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("dotnet").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // Initialize
    let server_info = client.peer_info();
    match server_info {
        Some(info) => {
            println!("🔗 Connected to server:");
            println!("   Name: {}", info.server_info.name);
            println!("   Version: {}", info.server_info.version);
            println!("   Protocol: {:?}", info.protocol_version);
            if let Some(instructions) = &info.instructions {
                println!("    Instructions: {}", instructions);
            }
            
            // Display capabilities
            println!("   Capabilities:");
            if info.capabilities.tools.is_some() {
                println!("   • Tools support enabled");
            }
            if info.capabilities.resources.is_some() {
                println!("   • Resources support enabled");
            }
            if info.capabilities.prompts.is_some() {
                println!("   • Prompts support enabled");
            }
            if info.capabilities.completions.is_some() {
                println!("   • Completions support enabled");
            }
            if info.capabilities.logging.is_some() {
                println!("   • Logging support enabled");
            }
        }
        None => {
            println!("🔗 Connected to server (no info available)");
        }
    }

    // List tools
    let tools = client.list_tools(Default::default()).await?;
    println!("📋 Available tools: {}", tools.tools.len());
    for tool in &tools.tools {
        println!("   • {} - {}",
            tool.name,
            tool.description.as_deref().unwrap_or("No description")
        );
    }

    // Call add tool with arguments = {"a": 3, "b": 2}
    let a = 3;
    let b = 2;

    println!("\n🧮 Calculating {} + {}...", a, b);
    let tool_result = client
        .call_tool(CallToolRequestParam {
            name: "add".into(),
            arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
        })
        .await?;

    // Parse and display result
    match &tool_result.content.first() {
        Some(content) => {
            match &content.raw {
                rmcp::model::RawContent::Text(text_content) => {
                    println!("✅ Result: {}", text_content.text);
                }
                other => {
                    println!("✅ Result: {:?}", other);
                }
            }
        }
        None => {
            println!("⚠️  No result returned from tool");
        }
    }

    if let Some(error) = &tool_result.is_error {
        if *error {
            println!("❌ Tool reported an error");
        }
    }

    client.cancel().await?;
    Ok(())
}
