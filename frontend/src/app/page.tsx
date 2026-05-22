import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-3xl font-semibold mb-4">Welcome</h1>
        <p className="mb-6">Please sign in to continue.</p>
        <Link href="/login" className="px-4 py-2 bg-blue-600 text-white rounded">
          Sign in
        </Link>
      </div>
    </div>
  );
}
