import {
    Grid,
    GridItem,
} from "@chakra-ui/react";
import { NextSeo } from "next-seo";

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
                준비중
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
