import dayjs from "dayjs";
import fs from "fs";
import matter from "gray-matter";
import { serialize } from "next-mdx-remote/serialize";
import { join } from "path";
import {MDXRemoteSerializeResult} from "next-mdx-remote";

export const POSTS_PATH = join(process.cwd(), "src/posts/");
export const DEV_PATH = "dev";
export const NOTE_PATH = "note";
export const PS_PATH = "ps";
const paths = [DEV_PATH, NOTE_PATH, PS_PATH] as const

type PATHS = typeof paths[number]

type PostType = {
  slug: string;
  mdxSource : MDXRemoteSerializeResult<Record<string, unknown>>;
  content: string;
  data: {[p: string]: any};
  path: PATHS;
}

type PostReturnType = {
  posts: PostType[],
  total: number
}

const getSlugFromFileName = (path: PATHS, filePath: string) => {
  return {path: path, slug: filePath.replace(/\.mdx?$/, "")};
};

export const getPathSlugs = (path: PATHS)=> fs.readdirSync(POSTS_PATH+path).map((filename)=>getSlugFromFileName(path, filename))
const allPostSlugs: any[] = paths.map((path)=>fs.readdirSync(POSTS_PATH+path).map((filename)=>getSlugFromFileName(path, filename)))
export const getAllPostSlugs = [].concat(...allPostSlugs)

export const getPostBySlug = async (path: PATHS, slug: string) => {
  const postFilePath = join(POSTS_PATH+path, `${slug}.mdx`);
  const source = fs.readFileSync(postFilePath, "utf8");

  const { content, data } = matter(source);

  const mdxSource = await serialize(content);
  return {
    slug,
    content,
    mdxSource,
    data,
    path,
  };
};

export const getPathPosts :(path: PATHS)=> Promise<PostReturnType> = async (path) => {
  const allPosts = await Promise.all(
      getPathSlugs(path).map(async ({slug}) => await getPostBySlug(path, slug))
  );

  return {
    posts: allPosts.sort((a, b) =>
        dayjs(b.data.date).isAfter(a.data.date) ? 1 : -1
    ),
    total: allPosts.length,
  };
};

export const getAllPosts :()=> Promise<PostReturnType> = async () => {
  const allPostsByPath: any[] = await Promise.all(
      paths.map(async (path)=> await Promise.all(getPathSlugs(path).map(async ({slug})=> await getPostBySlug(path, slug)))))

  const allPosts: PostType[] = [].concat(...allPostsByPath)

  return {
    posts: allPosts.sort((a, b) =>
      dayjs(b.data.date).isAfter(a.data.date) ? 1 : -1
    ),
    total: allPosts.length,
  };
};

export const getTags = async () => {
  const { posts } = await getAllPosts();
  return posts.reduce((flat, next) => flat.concat(next.data.tags), []).sort();
};

export const getTagsWithOccurrences = async () => {
  const tags = await getTags();
  return tags.reduce(function (obj: any, item) {
    obj[item] = (obj[item] || 0) + 1;
    return obj;
  }, {});
};

export const getPostsByTag = async (tag: string) => {
  const { posts } = await getAllPosts();
  const filteredPosts = posts.filter((post) => post.data.tags.includes(tag));
  return {
    posts: filteredPosts,
    total: filteredPosts.length,
  };
};
