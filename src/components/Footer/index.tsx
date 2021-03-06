import {
  Box,
  chakra,
  Container,
  Stack,
  Text,
  useColorModeValue,
  VisuallyHidden,
} from "@chakra-ui/react";
import { ReactNode } from "react";
import { FaGithub } from "react-icons/fa";

const SocialButton = ({
  children,
  label,
  href,
}: {
  children: ReactNode;
  label: string;
  href: string;
}) => {
  return (
    <chakra.button
      rounded={"full"}
      w={8}
      h={8}
      cursor={"pointer"}
      as={"a"}
      href={href}
      display={"inline-flex"}
      alignItems={"center"}
      justifyContent={"center"}
      transition={"background 0.3s ease"}
      _hover={{
        bg: useColorModeValue("blackAlpha.200", "whiteAlpha.200"),
      }}
    >
      <VisuallyHidden>{label}</VisuallyHidden>
      {children}
    </chakra.button>
  );
};

const Footer = () => (
  <Box>
    <Container
      as={Stack}
      maxW={"6xl"}
      py={4}
      direction={{ base: "column", md: "row" }}
      spacing={4}
      justify={{ base: "center", md: "space-between" }}
      align={{ base: "center", md: "center" }}
    >
      <Text>© {new Date().getFullYear()} Seongwoon Jeong. All rights reserved</Text>
      <Stack direction={"row"} spacing={6}>
        <SocialButton label={"Github"} href={"https://github.com/Odysseyj"}>
          <FaGithub size={25}/>
        </SocialButton>
        <SocialButton label={"Backjoon"} href={"https://www.acmicpc.net/user/ggogumalove"}>
          <img width={30} height={30} src={useColorModeValue("/images/backjoon.png", "/images/backjoon-white.png")} />
        </SocialButton>
      </Stack>
    </Container>
  </Box>
);
export default Footer;
