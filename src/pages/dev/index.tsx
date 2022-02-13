import PostList from "@src/components/Posts";
import { POSTS_PER_PAGE } from "@src/lib/consts";
import {DEV_PATH, getPathPosts} from "@src/lib/posts";
import { NextPage } from "next";

const Dev: NextPage = ({ posts, total }: any) => (
  <>
    <PostList
      posts={posts}
      page={1}
      total={total}
      title={`Dev`}
      urlPrefix={`/dev`}
    />
  </>
);

export default Dev;

export const getStaticProps = async () => {
  const { posts, total } = await getPathPosts(DEV_PATH);

  return {
    props: {
      posts: posts.slice(0, POSTS_PER_PAGE),
      total,
    },
  };
};
