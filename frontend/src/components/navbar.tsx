"use client";

import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { signOut, useSession } from "next-auth/react";

const NAV_ITEMS = [
  { href: "/project", label: "Project" },
  { href: "/about", label: "About" },
  { href: "/contact", label: "Contact" },
  { href: "/people", label: "People" },
];

export default function Navbar() {
  const pathname = usePathname();
  const menuRef = useRef<HTMLDivElement | null>(null);
  const [open, setOpen] = useState(false);
  const { data: session } = useSession();

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  function handleLogout() {
    localStorage.removeItem("access_token");
    setOpen(false);
    signOut({ callbackUrl: "/login" });
  }

  const accountLabel = session?.user?.name || session?.user?.email || "Account";

  return (
    <header className="fixed inset-x-0 top-0 z-50 border-b border-slate-200 bg-white/95 backdrop-blur">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link href="/" className="flex items-center gap-3 font-semibold text-slate-900">
          <Image src="/favicon.ico" alt="FinancialAgent logo" width={32} height={32} className="rounded-md" />
          <span className="text-lg tracking-tight">FinancialAgent</span>
        </Link>

        <nav className="flex items-center gap-2 rounded-full border border-slate-200 bg-slate-50 p-1">
          {NAV_ITEMS.map((item) => {
            const active = pathname === item.href;
            return (
              <Link
                key={item.href}
                href={item.href}
                className={[
                  "rounded-full px-4 py-2 text-sm font-medium transition",
                  active
                    ? "bg-slate-900 text-white shadow-sm"
                    : "text-slate-600 hover:bg-white hover:text-slate-900",
                ].join(" ")}
              >
                {item.label}
              </Link>
            );
          })}
        </nav>

        <div className="relative" ref={menuRef}>
          <button
            type="button"
            onClick={() => setOpen((value) => !value)}
            className="flex items-center gap-3 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm hover:border-slate-300"
          >
            <span className="flex h-8 w-8 items-center justify-center rounded-full bg-slate-900 text-xs font-semibold text-white">
              {accountLabel
                .split(" ")
                .filter(Boolean)
                .slice(0, 2)
                .map((part) => part[0]?.toUpperCase())
                .join("") || "FA"}
            </span>
            <span>{accountLabel}</span>
          </button>

          {open ? (
            <div className="absolute right-0 mt-3 w-48 overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-xl">
              <Link
                href="/settings"
                onClick={() => setOpen(false)}
                className="block px-4 py-3 text-sm text-slate-700 hover:bg-slate-50"
              >
                Settings
              </Link>
              <button
                type="button"
                onClick={handleLogout}
                className="block w-full px-4 py-3 text-left text-sm text-red-600 hover:bg-red-50"
              >
                Log out
              </button>
            </div>
          ) : null}
        </div>
      </div>
    </header>
  );
}