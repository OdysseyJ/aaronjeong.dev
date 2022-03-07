import PostList from "@src/components/Posts";
import {getAllPosts, PostReturnType, PostType} from "@src/lib/posts";
import { NextPage } from "next";
import {Input, InputGroup, InputRightElement} from "@chakra-ui/input";
import {useRef, useState} from "react";
import {Button} from "@chakra-ui/react";

const Search: NextPage<PostReturnType> = ({ posts, total }) => {
    const [matchingPosts, setMatchingPosts] = useState<PostType[]>([])
    const ref = useRef<HTMLInputElement>(null)
    const handleSubmit = ()=>{
        if (ref.current){
            if (!ref.current.value)
                setMatchingPosts([])
            else
                setMatchingPosts(posts.filter((p)=>{
                    const lowerTitle = p.data.title.toLowerCase()
                    // @ts-ignore
                    const lowerSearchValues = ref.current.value.toLowerCase().split(" ")
                    return lowerSearchValues.filter((s)=>lowerTitle.includes(s)).length == lowerSearchValues.length
                }))
        }
    }
    const handleInputKeyUp = (event: React.KeyboardEvent<HTMLInputElement>)=>{
        if (event.code == "Enter"){
            handleSubmit()
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
        onKeyUp={handleInputKeyUp}
      />
      <InputRightElement width='4.5rem'>
        <Button h='1.75rem' size='sm' onClick={handleSubmit}>
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
