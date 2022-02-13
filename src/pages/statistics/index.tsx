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
import { getPosts } from "@src/lib/posts";
import { NextSeo } from "next-seo";
import NextLink from "next/link";

type HomeStaticProps = {
   allTexts: string
    counts: {
        ps: number,
        note : number,
        dev: number
    }
}

const Statistics = ({ allTexts, counts: {ps, note, dev} }: HomeStaticProps) => (
    <>
        <NextSeo title={"Statistics"} />
        <Grid
            templateColumns={{
                md: "repeat(12, 1fr)",
            }}
            gap={12}
        >
            <GridItem colSpan={{ md: 4 }}>
                Hello world
            </GridItem>
        </Grid>
    </>
);

export default Statistics;

export const getStaticProps = async () => {
    const psCount = 100
    const devCount = 100
    const noteCount = 100
    const allTexts = ""

    return {
        props: {
            allTexts : allTexts,
            counts : {
                "ps": psCount,
                "dev": devCount,
                "note": noteCount
            }
        },
    };
};
