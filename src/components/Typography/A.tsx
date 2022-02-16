import { Link } from "@chakra-ui/react";
import NextLink from "next/link";

const A: ({
  as,
  href,
  ...otherProps
}: {
  as: string;
  href: string;
  [p: string]: any;
}) => JSX.Element = ({ as, href, ...otherProps }) => (
  <NextLink as={as} href={href}>
    <Link href={href} color={`teal`} target={"_blank"} {...otherProps} />
  </NextLink>
);
export default A;
