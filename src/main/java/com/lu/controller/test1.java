package com.lu.controller;

import com.lu.pojo.User;
import org.springframework.http.RequestEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Controller
public class test1 {
    @RequestMapping("/index")
    public String index(){
        return "index";
    }
    @RequestMapping(value = "/testRequestBody",method = RequestMethod.POST)
    public String testRequestBody(@RequestBody String requestBody){
        System.out.println("请求体："+requestBody);
        return "success";
    }
    @PostMapping("/testRequestEntity")
    public String testRequestEntity(RequestEntity<String> requestEntity){
        System.out.println("请求头："+requestEntity.getHeaders());
        System.out.println("请求体："+requestEntity.getBody());
        return "success";
    }
    @RequestMapping("/testResponse")
    public void testResponse(HttpServletResponse httpServletResponse) throws IOException {
        httpServletResponse.getWriter().println("hello,response");
    }
    @RequestMapping("/testResponseBody")
    @ResponseBody
    public String testResponseBody(){
        return "hello,responseBody";
    }
    @RequestMapping("/testResponseUser")
    @ResponseBody
    public User testResponseUser(){
        System.out.println("test1");
        System.out.println("test2");
        System.out.println("test3");
        System.out.println("master test4");
        return new User(1001,"鲁文慧",'男',"123456");
    }
}
