export default function AddTool() {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold">Добави нов инструмент</h2>
      <form className="mt-4 space-y-4">
        <input type="text" placeholder="Име" className="w-full p-2 border rounded" />
        <input type="url" placeholder="Линк" className="w-full p-2 border rounded" />
        <textarea placeholder="Описание" className="w-full p-2 border rounded" />
        <button className="bg-blue-600 text-white px-4 py-2 rounded">Добави</button>
      </form>
    </div>
  )
}
