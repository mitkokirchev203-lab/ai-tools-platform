import ToolCard from "../components/ToolCard";

export default function Tools() {
  const sampleTools = [
    { id: 1, name: "ChatGPT", description: "AI Chatbot", link: "https://chat.openai.com" },
    { id: 2, name: "Stable Diffusion", description: "AI Image Generator", link: "https://stability.ai" }
  ];

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold">AI Tools</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
        {sampleTools.map(tool => (
          <ToolCard key={tool.id} tool={tool} />
        ))}
      </div>
    </div>
  )
}
