export type RoleName = "Admin" | "User" | string;

export type TokenPayload = {
  sub?: string;
  id?: string;
  role?: RoleName;
};

export type ProjectMember = {
  user_id: string;
  email: string;
  role_name: string;
};

export type ConversationCreator = {
  user_id: string;
  email: string;
  role_name: string;
};

export type ConversationRow = {
  conversation_id: string;
  project_id: string;
  title: string;
  creator?: ConversationCreator | null;
  created_at?: string | null;
  updated_at?: string | null;
};

export type ProjectRow = {
  project_id: string;
  name: string;
  description?: string | null;
  embedding_model: string;
  llm_model: string;
  member_ids: string[];
  members: ProjectMember[];
};

export type UserRow = {
  user_id: string;
  email: string;
  role_name: string;
};

export type ProjectPayload = {
  name: string;
  description?: string;
  embedding_model?: string;
  llm_model?: string;
  member_ids?: string[];
};

export type ConversationPayload = {
  title?: string;
};

export type ModelOption = {
  value: string;
  label: string;
};
