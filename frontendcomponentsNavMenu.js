import Link from "next/link"

export default function NavMenu() {
  return (
    <nav className="bg-gray-800 text-white p-4">
      <ul className="flex space-x-4">
        <li><Link href="/">Home</Link></li>
        <li><Link href="/dashboard">Dashboard</Link></li>
        <li><Link href="/tools">Tools</Link></li>
        <li><Link href="/add-tool">Add Tool</Link></li>
        <li><Link href="/profile">Profile</Link></li>
        <li><Link href="/admin-panel">Admin</Link></li>
      </ul>
    </nav>
  )
}
