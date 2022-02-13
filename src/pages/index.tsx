import {
  Avatar,
  Badge,
  Box,
  Center,
  Grid,
  GridItem,
  Heading,
  Link,
  Stack,
  StackDivider,
  Text,
  useColorModeValue,
  VStack,
} from "@chakra-ui/react";
import PostItem from "@src/components/Posts/PostItem";
import { H2 } from "@src/components/Typography/Headings";
import { getAllPosts } from "@src/lib/posts";
import { NextSeo } from "next-seo";

const Home = ({ posts }: any) => (
  <>
    <NextSeo title={"Home"} />
    <Grid
      templateColumns={{
        md: "repeat(12, 1fr)",
      }}
      gap={12}
    >
      <GridItem colSpan={{ md: 4 }}>
        <Center>
          <Box
            maxW={{ base: "320px", md: "100%" }}
            w={"full"}
            bg={useColorModeValue("white", "whiteAlpha.100")}
            boxShadow={"2xl"}
            rounded={"lg"}
            p={6}
            textAlign={"center"}
          >
            <Avatar
              size={"2xl"}
              alt={"Aaron"}
              mb={4}
              pos={"relative"}
            />
            <Heading fontSize={"2xl"} fontFamily={"body"}>
              Seongwoon Jeong
            </Heading>
            <Text fontWeight={600} color={"gray.500"} mb={4}>
              @Aaron
            </Text>
            <Text
              textAlign={"center"}
              color={useColorModeValue("gray.700", "gray.400")}
              px={3}
            >
              Python /
              Javascript
              Developer
            </Text>

            <Stack align={"center"} justify={"center"} direction={"row"} mt={6}>
              <Badge
                px={2}
                py={1}
                bg={useColorModeValue("gray.50", "gray.800")}
                fontWeight={"400"}
              >
                #PYTHON
              </Badge>
              <Badge
                px={2}
                py={1}
                bg={useColorModeValue("gray.50", "gray.800")}
                fontWeight={"400"}
              >
                #REACTJS
              </Badge>
              <Badge
                px={2}
                py={1}
                bg={useColorModeValue("gray.50", "gray.800")}
                fontWeight={"400"}
              >
                #VIM
              </Badge>
            </Stack>
          </Box>
        </Center>
      </GridItem>
      <GridItem colSpan={{ md: 8 }}>
        <Box>
          <H2>최근 글</H2>
          <VStack
            divider={<StackDivider borderColor="gray.200" />}
            spacing={2}
            align="stretch"
            mb={2}
          >
            {posts &&
              posts.map((post: any) => <PostItem key={post.slug} post={post} />)}
          </VStack>
        </Box>
      </GridItem>
    </Grid>
  </>
);

export default Home;

export const getStaticProps = async () => {
  const { posts, total } = await getAllPosts();

  return {
    props: {
      posts: posts.slice(0, 5),
      total,
    },
  };
};
