export default function ToolCard({ tool }) {
  return (
    <div className="border rounded p-4 bg-white shadow">
      <h3 className="text-xl font-bold">{tool.name}</h3>
      <p className="text-gray-600">{tool.description}</p>
      <a href={tool.link} target="_blank" rel="noreferrer" className="text-blue-600 mt-2 inline-block">
        Виж повече
      </a>
    </div>
  )
}
