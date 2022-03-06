import PostList from "@src/components/Posts";
import {getAllPosts, PostReturnType, PostType} from "@src/lib/posts";
import { NextPage } from "next";
import {Input, InputGroup, InputRightElement} from "@chakra-ui/input";
import {useRef, useState} from "react";
import {Button} from "@chakra-ui/react";

const Search: NextPage<PostReturnType> = ({ posts, total }) => {
    const [matchingPosts, setMatchingPosts] = useState<PostType[]>([])
    const ref = useRef<HTMLInputElement>(null)
    const handleSearch = ()=>{
        if (ref.current && ref.current.value){
            // @ts-ignore
            setMatchingPosts(posts.filter((p)=>p.data.title.toLowerCase().includes(ref.current.value)))
        }
    }
    return (<>
    <InputGroup size='md'>
      <Input
        pr='4.5rem'
        placeholder='검색어를 입력하세요.'
        size={"md"}
        variant={"filled"}
        ref={ref}
      />
      <InputRightElement width='4.5rem'>
        <Button h='1.75rem' size='sm' onClick={handleSearch}>
          {"검색"}
        </Button>
      </InputRightElement>
    </InputGroup>
    <PostList
        posts={matchingPosts}
        title={`검색결과`}
    />
    </>)
};

export default Search;

export const getStaticProps = async () => {
    const { posts, total } = await getAllPosts();

    return {
        props: {
            posts: posts,
            total,
        },
    };
};
