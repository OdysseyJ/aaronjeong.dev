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
import {getAllPosts, getPostsByDate} from "@src/lib/posts";
import { NextSeo } from "next-seo";
import HeatMap from "@src/components/Charts/HeatMap";

const Home = ({ posts, postsByDate }: any) => (
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
  const { posts: postsByDate } = await getPostsByDate();

  return {
    props: {
      posts: posts.slice(0, 10),
      postsByDate: postsByDate,
      total,
    },
  };
};
