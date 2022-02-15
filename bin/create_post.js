#!/usr/bin/env node

const { join } = require("path");
const matter = require("gray-matter");
const { prompt } = require("enquirer");
const fs = require("fs");
const dayjs = require("dayjs");
const POSTS_PATH = join(process.cwd(), "src/posts");
const slugify = require("slugify");

const getFilePath = (directory, filename) => {
  const slug = slugify(filename, {
    strict: true,
    lower: true,
  });
  return join(POSTS_PATH+`/${directory}`, `${dayjs().format("YYYY-MM-DD")}-${slug}.mdx`);
};

prompt([
  {
    type: "input",
    name: "directory",
    message: `Where do you want to write?`,
    required: true,
    validate: (directory) => {
      return fs.existsSync(POSTS_PATH+`/${directory}/`)
          ? true
          : "directory not exist";
    },
  }]).then((r)=>{
  const { directory } = r;
    prompt([
  {
    type: "input",
        name: "filename",
      message: `What is the file name?`,
      required: true,
      validate: (filename) => {
    return fs.existsSync(getFilePath(directory, filename))
        ? `${getFilePath(directory, filename)} exists.`
        : true;
  },
  },
  {
    type: "input",
        name: "title",
      message: "What is the post title?",
      required: true,
  },
  {
    type: "input",
        name: "description",
      message: "What is the post description?",
  },
])
.then((response) => {
    const { title, description, filename } = response;
    const filePath = getFilePath(directory, filename);
    const data = matter.stringify("", {
      title: title,
      description: description,
      date: `${dayjs().format()}`,
      tags: [],
    });

    fs.writeFileSync(filePath, data);
    console.log(`Post ${title} was created at ${filePath}`);
    console.log(data);
  })
      .catch(console.log);
})
