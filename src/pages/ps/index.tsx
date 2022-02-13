import PostList from "@src/components/Posts";
import { POSTS_PER_PAGE } from "@src/lib/consts";
import {getPathPosts,  PS_PATH} from "@src/lib/posts";
import { NextPage } from "next";

const Ps: NextPage = ({ posts, total }) => (
  <>
    <PostList
      posts={posts}
      page={1}
      total={total}
      title={`PS`}
      urlPrefix={`/ps`}
    />
  </>
);

export default Ps;

export const getStaticProps = async () => {
  const { posts, total } = await getPathPosts(PS_PATH);

  return {
    props: {
      posts: posts.slice(0, POSTS_PER_PAGE),
      total,
    },
  };
};
