import { useColorMode } from "@chakra-ui/react";
import { DiscussionEmbed } from "disqus-react";

type CommentsProps = {
  config: any
}

const Comments: React.FC<CommentsProps> = ({config}) => {
  const { colorMode } = useColorMode();

  return (
    <DiscussionEmbed
        shortname="aaronjeong"
        config={config}
    />
  );
};
export default Comments;
