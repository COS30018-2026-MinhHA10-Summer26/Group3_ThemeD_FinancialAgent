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

export type DocumentRow = {
  document_id: string;
  project_id: string;
  project_name: string;
  file_name: string;
  file_type?: string | null;
  file_path: string;
  total_page: number;
  total_chunk: number;
  uploader_email?: string | null;
  created_at?: string | null;
};

export type ChunkMetadataOriginalContent = {
  raw_text: string;
  tables_html: string[];
  images_base64: string[];
};

export type ChunkMetadata = {
  document_id: string;
  chunk_index: number;
  source: string | null;
  page: number | null;
  section_title: string | null;
  section_type: string | null;
  enhanced_content: string | null;
  original_content: ChunkMetadataOriginalContent | null;
};

export type ChunkRow = {
  chunk_id: string;
  document_id: string;
  content: string;
  chunk_index: number;
  token_count: number | null;
  chunk_metadata: ChunkMetadata | null;
  created_at: string | null;
};

export type DocumentChunksResponse = {
  document_id: string;
  file_name: string;
  total_chunk: number;
  chunks: ChunkRow[];
};

export type ModelOption = {
  value: string;
  label: string;
};
