import MainLayout from "./components/MainLayout/MainLayout";
import Editor from "./components/editor/editor";
import Preview from "./components/preview/preview";
import MarkdownProvider from "./providers/markdown-provider";

const MarkDown = () => (
  <MarkdownProvider>
    <MainLayout>
      <MainLayout.Column>
        <Editor />
      </MainLayout.Column>
      <MainLayout.Column>
        <Preview />
      </MainLayout.Column>
    </MainLayout>
  </MarkdownProvider>
);

export default MarkDown;
