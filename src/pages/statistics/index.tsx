import {
    Box,
    Grid,
    GridItem, Text,
} from "@chakra-ui/react";
import { NextSeo } from "next-seo";
import WordCloud from "@src/components/Charts/WordCloud";
import PieChart from "@src/components/Charts/Pie";
import {getAllPosts, getPathPosts, getPathSlugs} from "@src/lib/posts";
import HeatMap from "@src/components/Charts/HeatMap";

type HomeStaticProps = {
   texts: {
       ps: string,
       note: string,
       dev: string
   },
    counts: {
        ps: number,
        note : number,
        dev: number
    }
}

const Statistics = ({ texts: {note: note_text}, counts: {ps, note, dev} }: HomeStaticProps) => (
    <>
        <NextSeo title={"Statistics"} />
        <Text fontWeight={600} fontSize={"24px"} >
            Note에서 많이 사용한 단어
        </Text>
        <WordCloud allTexts={note_text}/>
        <Text fontWeight={600} fontSize={"24px"} mt={10} >
            게시판별 글의 개수
        </Text>
        <PieChart data={[{key: 'ps', value: ps}, {key: "note", value: note}, {key: "dev", value: dev}]}/>
        <Box padding={"10px"}/>
        {/*<HeatMap width={500} height={200} data={[]}/>*/}
    </>
);

export default Statistics;

export const getStaticProps = async () => {
    const {posts: note_posts, total: note_total} = await getPathPosts("note")
    const ps_total = getPathSlugs("ps").length
    const dev_total = getPathSlugs("dev").length
    const allNoteTexts =note_posts.map((p)=>p.content).join(" ")

    return {
        props: {
            texts : {
                "ps": "",
                "dev": "",
                "note": allNoteTexts
            },
            counts : {
                "ps": ps_total,
                "dev": dev_total,
                "note": note_total
            }
        },
    };
};
