#!/usr/bin/env node
const dotenv = require('dotenv')
dotenv.config()

const { join } = require("path");
const { prompt } = require("enquirer");
const fs = require("fs");
const dayjs = require("dayjs");
const slugify = require("slugify");
const AWS = require('aws-sdk');
const multer = require("multer");
const multerS3 = require("multer-s3");

const { AWS_REGION, AWS_IDENTITYPOOLID, AWS_BUCKET, SCREENSHOT_PATH  } = process.env

AWS.config.update({
  region : AWS_REGION,
  credentials : new AWS.CognitoIdentityCredentials({
    IdentityPoolId: AWS_IDENTITYPOOLID
})
})

const s3 = new AWS.S3({
  apiVersion: "2006-03-01",
  params: {Bucket: AWS_BUCKET}
});

const upload = multer({
  storage: multerS3({
    s3: s3,
    bucket: AWS_BUCKET,
    contentType: multerS3.AUTO_CONTENT_TYPE,
    acl: "public-read",
    key: (req, file, cb) => {
      let extension = path.extname(file.originalname)
      cb(null, 'profileimage/'+Date.now().toString()+extension);
    }
  }),
  limits: { fileSize: 5 * 1024 * 1024 }
});

const getFilePath = (filename, extension) => {
    const slug = slugify(filename, {
        strict: true,
        lower: true,
    });
    return join(SCREENSHOT_PATH, `${dayjs().format("YYYY-MM-DD")}-${slug}.${extension}`);
};

prompt([
    {
        type: "input",
        name: "filename",
        message: `File?`,
        required: true,
        validate: (filename) => {
            const allow_extensions = ["png", "jpg", "jpeg"]
            const is_valid = allow_extensions.map((extension)=>{
                return fs.existsSync(join(SCREENSHOT_PATH, `${filename}.${extension}`))
            }).filter((t)=>t).length !== 0
            return is_valid
                ? true
                : "file not exist";
        },
    }
]).then((r)=>{
    const { filename } = r;
    prompt([
        {
            type: "input",
            name: "prefix",
            message: `Prefix?`,
            required: true,
        },
    ]).then((response) => {
        const { prefix } = response
        console.log(filename)
        console.log(prefix);
    }).catch(console.log);
})
