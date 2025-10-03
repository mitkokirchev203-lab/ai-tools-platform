import NavMenu from "./NavMenu"

export default function Layout({ children }) {
  return (
    <div>
      <NavMenu />
      <main className="max-w-5xl mx-auto">{children}</main>
    </div>
  )
}
