const memoryCache = new Map<string, string>();
const storagePrefix = "finagent:page-cache:";

function hasStorage() {
  return typeof window !== "undefined";
}

function storageKey(key: string) {
  return `${storagePrefix}${key}`;
}

export function readPageCache<T>(key: string): T | null {
  if (memoryCache.has(key)) {
    const cachedValue = memoryCache.get(key);
    if (!cachedValue) return null;

    try {
      return JSON.parse(cachedValue) as T;
    } catch {
      return null;
    }
  }

  if (!hasStorage()) return null;

  try {
    const cachedValue = window.sessionStorage.getItem(storageKey(key));
    if (!cachedValue) return null;

    memoryCache.set(key, cachedValue);
    return JSON.parse(cachedValue) as T;
  } catch {
    return null;
  }
}

export function writePageCache<T>(key: string, value: T): void {
  try {
    const serialized = JSON.stringify(value);
    memoryCache.set(key, serialized);

    if (!hasStorage()) return;

    window.sessionStorage.setItem(storageKey(key), serialized);
  } catch {
    // Ignore cache write failures; the page can still load from the network.
  }
}
