import type { ConversationRow } from "@/components/project-detail/types";

type ProjectConversationsCardProps = {
  conversations: ConversationRow[];
  creatingConversation: boolean;
  hasProject: boolean;
  onCreateConversation: () => void;
  onOpenConversation: (conversationId: string) => void;
};

export function ProjectConversationsCard({
  conversations,
  creatingConversation,
  hasProject,
  onCreateConversation,
  onOpenConversation,
}: ProjectConversationsCardProps) {
  return (
    <div className="mt-6 rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-sm font-medium uppercase tracking-[0.2em] text-slate-500">Conversations</p>
          <h3 className="mt-2 text-xl font-semibold">Project chat sessions</h3>
          <p className="mt-1 text-sm text-slate-500">Any project member can start a conversation here.</p>
        </div>

        <button
          type="button"
          onClick={onCreateConversation}
          disabled={creatingConversation || !hasProject}
          className="rounded-full bg-slate-900 px-5 py-2.5 text-sm font-medium text-white hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-60"
        >
          {creatingConversation ? "Creating..." : "New conversation"}
        </button>
      </div>

      <div className="mt-5 grid gap-3 md:grid-cols-2 xl:grid-cols-3">
        {conversations.length > 0 ? (
          conversations.map((conversation) => (
            <button
              key={conversation.conversation_id}
              type="button"
              onClick={() => onOpenConversation(conversation.conversation_id)}
              className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4 text-left transition hover:border-slate-300 hover:bg-white"
            >
              <div className="font-medium text-slate-900">{conversation.title}</div>
              <div className="mt-1 text-sm text-slate-500">
                Creator: {conversation.creator?.email || "Unknown"}{" "}
                {conversation.creator?.role_name ? `(${conversation.creator.role_name})` : ""}
              </div>
            </button>
          ))
        ) : (
          <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-500 md:col-span-2 xl:col-span-3">
            No conversations yet. Create one to start chatting.
          </div>
        )}
      </div>
    </div>
  );
}
