import { ChevronLeftIcon, ChevronRightIcon } from "@chakra-ui/icons";
import {
    Box, Button,
    Flex,
    Link,
    Spacer,
    StackDivider,
    VStack,
} from "@chakra-ui/react";
import PostItem from "@src/components/Posts/PostItem";
import { H2 } from "@src/components/Typography/Headings";
import { POSTS_PER_PAGE } from "@src/lib/consts";
import { NextSeo } from "next-seo";
import NextLink from "next/link";

const PostList = ({ posts, page, total, title, urlPrefix }: any) => {
  const allPageCount = Math.ceil(total / POSTS_PER_PAGE)
  const hasNextPage = allPageCount > page;
  const hasPreviousPage = page > 1;
  const pageTitle = `${title} ${hasPreviousPage ? ` - Page ${page}` : ""}`;

  return (
    <>
      <NextSeo title={pageTitle} />
      <H2>{pageTitle}</H2>
      <VStack
        divider={<StackDivider borderColor="gray.200" />}
        spacing={2}
        align="stretch"
      >
        {posts && (
          <>
            {posts.map((post: any) => (
              <PostItem key={post.slug} post={post} />
            ))}
          </>
        )}
      </VStack>
      {posts && (
        <Flex my={4}>
          <Box>
            {hasPreviousPage && (
              <NextLink href={urlPrefix + `/${page - 1}`} passHref>
                  <Button variant="outline" colorScheme="blue">
                    <Link>
                      <ChevronLeftIcon /> 이전 {page - 1}/{allPageCount}
                    </Link>
                  </Button>
              </NextLink>
            )}
          </Box>
          <Spacer />
          <Box>
            {hasNextPage && (
              <NextLink href={urlPrefix + `/${page + 1}`} passHref>
                  <Button variant="outline" colorScheme="blue">
                    <Link>
                      다음 {page + 1}/{allPageCount} <ChevronRightIcon />
                    </Link>
                  </Button>
              </NextLink>
            )}
          </Box>
        </Flex>
      )}
    </>
  );
};

export default PostList;
