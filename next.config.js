/** @type {import('next').NextConfig} */
module.exports = {
  images:{
    domains: ['seongwoon-blog.s3.ap-northeast-2.amazonaws.com']
  },
  env: {
    host: "https://aaronjeong.dev",
    github: "https://github.com/Odysseyj",
    repo: "https://github.com/Odysseyj/aaronjeong.dev",
    title: "Aaron",
    title_template: "%s | aaron dev blog",
    description: "Python/Javascript Developer",
    measurement_id: "G-Q4JYBKTD35"
  },
  reactStrictMode: true,
  swcMinify: true,
};
