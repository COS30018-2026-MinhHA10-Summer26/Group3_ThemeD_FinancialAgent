"use client";

import { useEffect } from "react";
import { useSession } from "next-auth/react";

export default function AuthSync() {
  const { data: session, status } = useSession();

  useEffect(() => {
    const backendToken = (session as { backendToken?: string } | null)?.backendToken;

    if (status === "authenticated" && backendToken) {
      localStorage.setItem("access_token", backendToken);
      return;
    }

    if (status === "unauthenticated") {
      localStorage.removeItem("access_token");
    }
  }, [session, status]);

  return null;
}