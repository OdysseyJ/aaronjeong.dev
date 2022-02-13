import PostList from "@src/components/Posts";
import {POSTS_PER_PAGE} from "@src/lib/consts";
import {getPathPosts, PS_PATH, getPathSlugs} from "@src/lib/posts";

const PsPerPage = ({ posts, page, total }: any) => (
  <PostList
    posts={posts}
    page={page}
    total={total}
    title={`PS`}
    urlPrefix={`/ps`}
  />
);

export default PsPerPage;

export const getStaticPaths = async () => {
  const pages = Math.ceil(getPathSlugs(PS_PATH).length / POSTS_PER_PAGE);
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
  const { posts, total } = await getPathPosts(PS_PATH);

  return {
    props: {
      posts: posts.slice((page - 1) * POSTS_PER_PAGE, page * POSTS_PER_PAGE),
      page: Number(page),
      total,
    },
  };
};
