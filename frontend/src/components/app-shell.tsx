"use client";

import type { ReactNode } from "react";
import { usePathname } from "next/navigation";
import Navbar from "@/components/navbar";

const HIDDEN_PATHS = new Set(["/", "/login"]);

export default function AppShell({ children }: { children: ReactNode }) {
  const pathname = usePathname();
  const showNavbar = !HIDDEN_PATHS.has(pathname);

  return (
    <>
      {showNavbar ? <Navbar /> : null}
      <main className={showNavbar ? "flex-1 pt-20" : "flex-1"}>{children}</main>
    </>
  );
}