import PostList from "@src/components/Posts";
import { POSTS_PER_PAGE } from "@src/lib/consts";
import {DEV_PATH, getPathPosts, getPathSlugs} from "@src/lib/posts";

const DevPerPage = ({ posts, page, total }: any) => (
  <PostList
    posts={posts}
    page={page}
    total={total}
    title={`Dev`}
    urlPrefix={`/dev`}
  />
);

export default DevPerPage;

export const getStaticPaths = async () => {
  const pages = Math.ceil(getPathSlugs(DEV_PATH).length / POSTS_PER_PAGE);
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
  const { posts, total } = await getPathPosts(DEV_PATH);

  return {
    props: {
      posts: posts.slice((page - 1) * POSTS_PER_PAGE, page * POSTS_PER_PAGE),
      page: Number(page),
      total,
    },
  };
};
