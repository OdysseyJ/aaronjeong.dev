import {
    Grid,
    GridItem,
} from "@chakra-ui/react";
import { NextSeo } from "next-seo";
import WordCloud from "@src/components/Charts/WordCloud";

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
        <WordCloud />
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
