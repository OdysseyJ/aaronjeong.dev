import {Box, HStack, Spinner} from "@chakra-ui/react";
import Comments from "@src/components/Comments";
import MDXComponents from "@src/components/MDXComponents";
import TagLink from "@src/components/TagLink";
import { H2, H6 } from "@src/components/Typography/Headings";
import { getPostBySlug, getAllPostSlugs } from "@src/lib/posts";
import dayjs from "dayjs";
import { MDXRemote } from "next-mdx-remote";
import { ArticleJsonLd, NextSeo } from "next-seo";
import { useRouter } from "next/router";

const PostPage = ({ source, frontMatter, slug }: any) => {
  const router = useRouter();

  if (router.isFallback) {
    return <Spinner />;
  }

  const { title, description, date, tags } = frontMatter;
  const canonical = process.env.host + router.asPath;

  return (
    <>
      <NextSeo
        title={title}
        description={description}
        canonical={canonical}
        openGraph={{
          title: title,
          description: description,
          url: canonical,
          type: "article",
          article: {
            publishedTime: dayjs(date).toISOString(),
          },
        }}
        additionalMetaTags={[
          {
            name: "keywords",
            content: tags,
          },
        ]}
      />
      <ArticleJsonLd
        url={canonical}
        title={title}
        images={[]}
        datePublished={dayjs(date).format()}
        dateModified={dayjs(date).format()}
        authorName={["Aaron jeong"]}
        publisherName="Aaron jeong"
        publisherLogo={process.env.host + "/images/sweet-potato.png"}
        description={description}
      />
      <H2>{title}</H2>
      <H6>{dayjs(date).format("YYYY-MM-DD")}</H6>
      <HStack spacing={2} py={4}>
        {tags.map((tag: any) => (
            <TagLink key={tag} tag={tag} count={0} />
        ))}
      </HStack>
      <MDXRemote {...source} components={MDXComponents} />
      <Box padding={10}/>
      <Comments
        config={{
          url: canonical,
          identifier: slug,
          title: title,
          language: "ko"
        }}
      />
    </>
  );
};
export default PostPage;

export const getStaticProps = async ({ params }: any) => {
  const { slug, path } = params;
  const { mdxSource, data } = await getPostBySlug(path, slug);

  return {
    props: {
      source: mdxSource,
      frontMatter: data,
    },
  };
};

export const getStaticPaths = () => {
  return {
    paths: getAllPostSlugs.map(({path, slug}) => ({
      params: {
        slug: slug,
        path: path,
      },
    })),
    fallback: true,
  };
};
