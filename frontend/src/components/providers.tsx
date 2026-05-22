"use client";

import type { ReactNode } from "react";
import { SessionProvider } from "next-auth/react";
import AuthSync from "@/components/auth-sync";

export default function Providers({ children }: { children: ReactNode }) {
  return (
    <SessionProvider>
      <AuthSync />
      {children}
    </SessionProvider>
  );
}