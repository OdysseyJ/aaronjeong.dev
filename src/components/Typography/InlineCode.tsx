import { Code, useColorModeValue } from "@chakra-ui/react";
import { FC } from "react";

const InlineCode: FC = (props) => (
  <Code
    apply="mdx.code"
    color={useColorModeValue("red.800", "gray.200")}
    {...props}
  />
);
export default InlineCode;
