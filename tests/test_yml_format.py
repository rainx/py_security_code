#coding: utf-8

import six
import yaml
import os

"""
检测yml文件的格式

1 至少包含 digit_1 ， digit_1to3，
2 digit_1to3

里面只包含
    name -- [str],
    url? -- [str or list],
    tags? -- [list]
三个字段



"""

def test_yml_files_format():
    files = [
        "sse.yml",
        "szse.yml"
    ]

    for fname in files:
        sse_content = None
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "security_code", "exchange", fname)) as yaml_file:
            sse_content = yaml.load(yaml_file.read())

        if sse_content is None:
            raise Exception("can not find {}".format(fname))

        sse_digit_1 = sse_content['digit_1']
        sse_digit_1to3 = sse_content['digit_1to3']

        assert sse_digit_1 is not None
        assert type(sse_digit_1) == dict

        assert sse_digit_1to3 is not None
        assert type(sse_digit_1to3) == dict

        for k,v in sse_digit_1to3.items():
            assert type(v) == dict
            assert 'name' in v
            if 'url' in v:
                assert (type(v['url']) == six.text_type) or (type(v['url']) == six.binary_type) or (type(v['url']) == list)

            if 'tags' in v:
                assert type(v['tags']) == list

            for _k in v.keys():
                assert _k in ['url', 'name', 'tags']

if __name__ == '__main__':
    print("检测yaml文件格式是否合法, 建议使用pytest运行本程序，获取更多信息")
    test_yml_files_format()
    print("Done!")