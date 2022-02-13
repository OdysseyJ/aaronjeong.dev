import PostList from "@src/components/Posts";
import { POSTS_PER_PAGE } from "@src/lib/consts";
import {getPathPosts, NOTE_PATH} from "@src/lib/posts";
import { NextPage } from "next";

const Note: NextPage = ({ posts, total }) => (
  <>
    <PostList
      posts={posts}
      page={1}
      total={total}
      title={`Note`}
      urlPrefix={`/note`}
    />
  </>
);

export default Note;

export const getStaticProps = async () => {
    const { posts, total } = await getPathPosts(NOTE_PATH);

  return {
    props: {
      posts: posts.slice(0, POSTS_PER_PAGE),
      total,
    },
  };
};
