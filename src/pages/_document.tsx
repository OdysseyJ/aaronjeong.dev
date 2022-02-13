import { ColorModeScript } from "@chakra-ui/color-mode";
import Document, { Head, Html, Main, NextScript } from "next/document";
import GA from "@src/components/GA";

class MyDocument extends Document {
  render() {
    return (
      <Html lang="en">
        <Head>
            <GA/>
        </Head>
        <body>
          <ColorModeScript />
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
