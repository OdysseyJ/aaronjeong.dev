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
import {getAllPosts} from "@src/lib/posts";
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
              src={"/images/profile-image.jpeg"}
              mb={4}
              pos={"relative"}
            />
            <Heading fontSize={"2xl"} fontFamily={"body"}>
              Seongwoon Jeong
            </Heading>
            <Text fontWeight={600} color={"gray.500"} >
              ggogumalove@gmail.com
            </Text>
            <Text fontWeight={600} color={"gray.500"}>
              @Aaron
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
                #DJANGO
              </Badge>
            </Stack>
            <Stack align={"center"} justify={"center"} direction={"row"} mt={2}>
              <Badge
                  px={2}
                  py={1}
                  bg={useColorModeValue("gray.50", "gray.800")}
                  fontWeight={"400"}
              >
                #REACT
              </Badge>
              <Badge
                  px={2}
                  py={1}
                  bg={useColorModeValue("gray.50", "gray.800")}
                  fontWeight={"400"}
              >
                #NextJS
              </Badge>
            </Stack>
            <Stack align={"center"} justify={"center"} direction={"row"} mt={2}>
              <Badge
                  px={2}
                  py={1}
                  bg={useColorModeValue("gray.50", "gray.800")}
                  fontWeight={"400"}
              >
                #AWS
              </Badge>
              <Badge
                  px={2}
                  py={1}
                  bg={useColorModeValue("gray.50", "gray.800")}
                  fontWeight={"400"}
              >
                #Vim
              </Badge>
            </Stack>
            <Stack align={"center"} justify={"center"} direction={"column"} mt={5}>
              <Text fontWeight={600} color={"gray.500"} >
                아티클
              </Text>
              <Stack align={"center"} justify={"center"} direction={"column"} mt={2}>
                <Link style={{color: "blue"}} href="https://medium.com/team-turing/%EC%9D%B4%EB%B2%88-%EC%83%9D%EC%97%90-pm%EC%9D%80-%EC%B2%98%EC%9D%8C%EC%9D%B4%EB%9D%BC-%EC%88%98%ED%95%99-%EC%BD%98%ED%85%90%EC%B8%A0%EC%9A%A9-cms-%EC%A0%9C%EC%9E%91%EA%B8%B0-3dff51d835b2" target="_blank">
                  튜링 블로그 아티클
                </Link>
              </Stack>
            </Stack>
          </Box>
        </Center>
      </GridItem>
      <GridItem colSpan={{ md: 8 }}>
        <Box>
          <H2>Recents</H2>
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
      posts: posts.slice(0, 10),
      total,
    },
  };
};
