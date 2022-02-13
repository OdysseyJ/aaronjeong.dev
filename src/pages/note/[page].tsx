import PostList from "@src/components/Posts";
import { POSTS_PER_PAGE } from "@src/lib/consts";
import { getPathPosts, getPathSlugs, NOTE_PATH } from "@src/lib/posts";

const NotePerPage = ({ posts, page, total }: any) => (
  <PostList
    posts={posts}
    page={page}
    total={total}
    title={`Note`}
    urlPrefix={`/note`}
  />
);

export default NotePerPage;

export const getStaticPaths = async () => {
  const pages = Math.ceil(getPathSlugs(NOTE_PATH).length / POSTS_PER_PAGE);
  const paths = Array.from(Array(pages).keys()).map((page) => ({
    params: { page: String(page + 1) },
  }));

  return {
    paths,
    fallback: true,
  };
};

export const getStaticProps = async ({ params }: any) => {
  const { page } = params;
  const { posts, total } = await getPathPosts(NOTE_PATH);

  return {
    props: {
      posts: posts.slice((page - 1) * POSTS_PER_PAGE, page * POSTS_PER_PAGE),
      page: Number(page),
      total,
    },
  };
};
