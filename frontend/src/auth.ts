import NextAuth, { type NextAuthOptions } from "next-auth";
import GitHubProvider from "next-auth/providers/github";
import GoogleProvider from "next-auth/providers/google";
import { apiClient } from "@/lib/api";

async function mintBackendToken(email: string, name: string | undefined, provider: string) {
  const response = await apiClient.post("/auth/social-login", {
    email,
    name,
    provider,
  });

  return response.data as { access_token: string; role: string };
}

export const authOptions: NextAuthOptions = {
  session: {
    strategy: "jwt",
  },
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID ?? "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET ?? "",
    }),
    GitHubProvider({
      clientId: process.env.GITHUB_CLIENT_ID ?? "",
      clientSecret: process.env.GITHUB_CLIENT_SECRET ?? "",
    }),
  ],
  callbacks: {
    async jwt({ token, account, profile }) {
      if (account && profile && account.provider) {
        const email = (profile as { email?: string }).email ?? token.email;
        const name = (profile as { name?: string }).name ?? token.name ?? undefined;

        if (email) {
          const backendSession = await mintBackendToken(email, name, account.provider);
          token.backendToken = backendSession.access_token;
          token.backendRole = backendSession.role;
          token.email = email;
          token.name = name ?? token.name;
        }
      }

      return token;
    },
    async session({ session, token }) {
      (session as { backendToken?: string; role?: string }).backendToken = token.backendToken as string | undefined;
      (session as { backendToken?: string; role?: string }).role = token.backendRole as string | undefined;

      if (session.user) {
        session.user.email = token.email ?? session.user.email ?? undefined;
        session.user.name = token.name ?? session.user.name ?? undefined;
      }

      return session;
    },
  },
  pages: {
    signIn: "/login",
  },
  secret: process.env.NEXTAUTH_SECRET,
};

export default NextAuth(authOptions);