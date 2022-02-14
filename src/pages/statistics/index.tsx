import {
    Grid,
    GridItem,
} from "@chakra-ui/react";
import { NextSeo } from "next-seo";
import WordCloud from "@src/components/Charts/WordCloud";
import PieChart from "@src/components/Charts/Pie";
import {getPathSlugs} from "@src/lib/posts";
import HeatMap from "@src/components/Charts/HeatMap";

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
        <PieChart data={[{key: 'ps', value: ps}, {key: "note", value: note}, {key: "dev", value: dev}]}/>
        <HeatMap/>
    </>
);

export default Statistics;

export const getStaticProps = async () => {
    const psCount = getPathSlugs("ps").length
    const devCount = getPathSlugs("dev").length
    const noteCount = getPathSlugs("note").length
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
