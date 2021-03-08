import setuptools


setuptools.setup(
    name="tg-notify-send", 
    version="0.0.2",
    author="Peter Ibragimov",
    author_email="peter.ibragimov@gmail.com",
    description="Little terminal command for notifing in telegram",
    url="https://github.com/TeaDove/tf-notify-send",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points = {
        'console_scripts': ['tg-notify-send=src.main:main']
    },
    install_requires=[
        'requests>=2.22.0',
    ]
)
