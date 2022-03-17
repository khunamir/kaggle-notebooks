{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ca0d0dee",
   "metadata": {
    "_cell_guid": "d0e4698f-5240-4af3-8925-d9ebaa56fe5b",
    "_uuid": "d74a9821-0c6f-4e13-b8b3-3319849b1760",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:28.787204Z",
     "iopub.status.busy": "2022-03-17T08:05:28.786441Z",
     "iopub.status.idle": "2022-03-17T08:05:28.856713Z",
     "shell.execute_reply": "2022-03-17T08:05:28.857224Z",
     "shell.execute_reply.started": "2022-03-17T07:45:21.642191Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.108529,
     "end_time": "2022-03-17T08:05:28.857551",
     "exception": false,
     "start_time": "2022-03-17T08:05:28.749022",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/kaggle/input/reddit-vaccine-myths/reddit_vm.csv\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>score</th>\n",
       "      <th>id</th>\n",
       "      <th>url</th>\n",
       "      <th>comms_num</th>\n",
       "      <th>created</th>\n",
       "      <th>body</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Health Canada approves AstraZeneca COVID-19 va...</td>\n",
       "      <td>7</td>\n",
       "      <td>lt74vw</td>\n",
       "      <td>https://www.canadaforums.ca/2021/02/health-can...</td>\n",
       "      <td>0</td>\n",
       "      <td>1.614400e+09</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2021-02-27 06:33:45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>COVID-19 in Canada: 'Vaccination passports' a ...</td>\n",
       "      <td>2</td>\n",
       "      <td>lsh0ij</td>\n",
       "      <td>https://www.canadaforums.ca/2021/02/covid-19-i...</td>\n",
       "      <td>1</td>\n",
       "      <td>1.614316e+09</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2021-02-26 07:11:07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Coronavirus variants could fuel Canada's third...</td>\n",
       "      <td>6</td>\n",
       "      <td>lohlle</td>\n",
       "      <td>https://www.canadaforums.ca/2021/02/coronaviru...</td>\n",
       "      <td>0</td>\n",
       "      <td>1.613887e+09</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2021-02-21 07:50:08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Canadian government to extend COVID-19 emergen...</td>\n",
       "      <td>1</td>\n",
       "      <td>lnptv8</td>\n",
       "      <td>https://www.canadaforums.ca/2021/02/canadian-g...</td>\n",
       "      <td>0</td>\n",
       "      <td>1.613796e+09</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2021-02-20 06:35:13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Canada: Pfizer is 'extremely committed' to mee...</td>\n",
       "      <td>6</td>\n",
       "      <td>lkslm6</td>\n",
       "      <td>https://www.canadaforums.ca/2021/02/canada-pfi...</td>\n",
       "      <td>0</td>\n",
       "      <td>1.613468e+09</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2021-02-16 11:36:28</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  score      id  \\\n",
       "0  Health Canada approves AstraZeneca COVID-19 va...      7  lt74vw   \n",
       "1  COVID-19 in Canada: 'Vaccination passports' a ...      2  lsh0ij   \n",
       "2  Coronavirus variants could fuel Canada's third...      6  lohlle   \n",
       "3  Canadian government to extend COVID-19 emergen...      1  lnptv8   \n",
       "4  Canada: Pfizer is 'extremely committed' to mee...      6  lkslm6   \n",
       "\n",
       "                                                 url  comms_num       created  \\\n",
       "0  https://www.canadaforums.ca/2021/02/health-can...          0  1.614400e+09   \n",
       "1  https://www.canadaforums.ca/2021/02/covid-19-i...          1  1.614316e+09   \n",
       "2  https://www.canadaforums.ca/2021/02/coronaviru...          0  1.613887e+09   \n",
       "3  https://www.canadaforums.ca/2021/02/canadian-g...          0  1.613796e+09   \n",
       "4  https://www.canadaforums.ca/2021/02/canada-pfi...          0  1.613468e+09   \n",
       "\n",
       "  body            timestamp  \n",
       "0  NaN  2021-02-27 06:33:45  \n",
       "1  NaN  2021-02-26 07:11:07  \n",
       "2  NaN  2021-02-21 07:50:08  \n",
       "3  NaN  2021-02-20 06:35:13  \n",
       "4  NaN  2021-02-16 11:36:28  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "        \n",
    "df = pd.read_csv(\"/kaggle/input/reddit-vaccine-myths/reddit_vm.csv\")\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "de3d9110",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:28.921386Z",
     "iopub.status.busy": "2022-03-17T08:05:28.920721Z",
     "iopub.status.idle": "2022-03-17T08:05:28.945761Z",
     "shell.execute_reply": "2022-03-17T08:05:28.944997Z",
     "shell.execute_reply.started": "2022-03-17T07:45:22.224539Z"
    },
    "papermill": {
     "duration": 0.06258,
     "end_time": "2022-03-17T08:05:28.945921",
     "exception": false,
     "start_time": "2022-03-17T08:05:28.883341",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>score</th>\n",
       "      <th>comms_num</th>\n",
       "      <th>created</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1602.000000</td>\n",
       "      <td>1602.000000</td>\n",
       "      <td>1.602000e+03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.686642</td>\n",
       "      <td>1.838951</td>\n",
       "      <td>1.547197e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>29.915671</td>\n",
       "      <td>16.115147</td>\n",
       "      <td>7.099511e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-12.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.389595e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.554367e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.569226e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.584901e+09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1187.000000</td>\n",
       "      <td>595.000000</td>\n",
       "      <td>1.640822e+09</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             score    comms_num       created\n",
       "count  1602.000000  1602.000000  1.602000e+03\n",
       "mean      3.686642     1.838951  1.547197e+09\n",
       "std      29.915671    16.115147  7.099511e+07\n",
       "min     -12.000000     0.000000  1.389595e+09\n",
       "25%       1.000000     0.000000  1.554367e+09\n",
       "50%       1.000000     0.000000  1.569226e+09\n",
       "75%       3.000000     1.000000  1.584901e+09\n",
       "max    1187.000000   595.000000  1.640822e+09"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ce01e747",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:29.006582Z",
     "iopub.status.busy": "2022-03-17T08:05:29.005809Z",
     "iopub.status.idle": "2022-03-17T08:05:29.009758Z",
     "shell.execute_reply": "2022-03-17T08:05:29.009086Z",
     "shell.execute_reply.started": "2022-03-17T07:45:22.665913Z"
    },
    "papermill": {
     "duration": 0.036855,
     "end_time": "2022-03-17T08:05:29.009919",
     "exception": false,
     "start_time": "2022-03-17T08:05:28.973064",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['title', 'score', 'id', 'url', 'comms_num', 'created', 'body',\n",
       "       'timestamp'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a2e6be59",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:29.071619Z",
     "iopub.status.busy": "2022-03-17T08:05:29.069851Z",
     "iopub.status.idle": "2022-03-17T08:05:29.075677Z",
     "shell.execute_reply": "2022-03-17T08:05:29.076270Z",
     "shell.execute_reply.started": "2022-03-17T07:45:22.865613Z"
    },
    "papermill": {
     "duration": 0.040286,
     "end_time": "2022-03-17T08:05:29.076490",
     "exception": false,
     "start_time": "2022-03-17T08:05:29.036204",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "376"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.isnull(df['body']).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "431e162e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:29.135433Z",
     "iopub.status.busy": "2022-03-17T08:05:29.134411Z",
     "iopub.status.idle": "2022-03-17T08:05:29.153152Z",
     "shell.execute_reply": "2022-03-17T08:05:29.153751Z",
     "shell.execute_reply.started": "2022-03-17T07:45:23.061609Z"
    },
    "papermill": {
     "duration": 0.049042,
     "end_time": "2022-03-17T08:05:29.153973",
     "exception": false,
     "start_time": "2022-03-17T08:05:29.104931",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>score</th>\n",
       "      <th>id</th>\n",
       "      <th>url</th>\n",
       "      <th>comms_num</th>\n",
       "      <th>created</th>\n",
       "      <th>body</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Fuck you anti-vaxxing retards</td>\n",
       "      <td>10</td>\n",
       "      <td>g6jkhp</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>8</td>\n",
       "      <td>1.587663e+09</td>\n",
       "      <td>https://youtu.be/zBkVCpbNnkU</td>\n",
       "      <td>2020-04-23 20:23:42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>Is it biologically possible to insert a 5G tra...</td>\n",
       "      <td>9</td>\n",
       "      <td>khzpug</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>9</td>\n",
       "      <td>1.608647e+09</td>\n",
       "      <td>Although I don't believe this to be true about...</td>\n",
       "      <td>2020-12-22 16:19:39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>134</th>\n",
       "      <td>I don't see any reason to trust J&amp;J with a vac...</td>\n",
       "      <td>0</td>\n",
       "      <td>ocj9ws</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>4</td>\n",
       "      <td>1.625288e+09</td>\n",
       "      <td>**”…the company knew there was asbestos in pro...</td>\n",
       "      <td>2021-07-03 07:57:05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>Vaccine Survey</td>\n",
       "      <td>0</td>\n",
       "      <td>ak5ziq</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>5</td>\n",
       "      <td>1.548543e+09</td>\n",
       "      <td>Hi guys! I was wondering if you could help me ...</td>\n",
       "      <td>2019-01-27 00:42:09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>161</th>\n",
       "      <td>Can I have a rant please??</td>\n",
       "      <td>13</td>\n",
       "      <td>o6nqcm</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>1</td>\n",
       "      <td>1.624488e+09</td>\n",
       "      <td>Not sure if the sub allows this but I need to ...</td>\n",
       "      <td>2021-06-24 01:35:24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 title  score      id  \\\n",
       "7                        Fuck you anti-vaxxing retards     10  g6jkhp   \n",
       "119  Is it biologically possible to insert a 5G tra...      9  khzpug   \n",
       "134  I don't see any reason to trust J&J with a vac...      0  ocj9ws   \n",
       "145                                     Vaccine Survey      0  ak5ziq   \n",
       "161                         Can I have a rant please??     13  o6nqcm   \n",
       "\n",
       "                                                   url  comms_num  \\\n",
       "7    https://www.reddit.com/r/VaccineMyths/comments...          8   \n",
       "119  https://www.reddit.com/r/VaccineMyths/comments...          9   \n",
       "134  https://www.reddit.com/r/VaccineMyths/comments...          4   \n",
       "145  https://www.reddit.com/r/VaccineMyths/comments...          5   \n",
       "161  https://www.reddit.com/r/VaccineMyths/comments...          1   \n",
       "\n",
       "          created                                               body  \\\n",
       "7    1.587663e+09                       https://youtu.be/zBkVCpbNnkU   \n",
       "119  1.608647e+09  Although I don't believe this to be true about...   \n",
       "134  1.625288e+09  **”…the company knew there was asbestos in pro...   \n",
       "145  1.548543e+09  Hi guys! I was wondering if you could help me ...   \n",
       "161  1.624488e+09  Not sure if the sub allows this but I need to ...   \n",
       "\n",
       "               timestamp  \n",
       "7    2020-04-23 20:23:42  \n",
       "119  2020-12-22 16:19:39  \n",
       "134  2021-07-03 07:57:05  \n",
       "145  2019-01-27 00:42:09  \n",
       "161  2021-06-24 01:35:24  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.dropna()\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "83eb47b1",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:29.213681Z",
     "iopub.status.busy": "2022-03-17T08:05:29.212911Z",
     "iopub.status.idle": "2022-03-17T08:05:29.217100Z",
     "shell.execute_reply": "2022-03-17T08:05:29.217776Z",
     "shell.execute_reply.started": "2022-03-17T07:49:41.559779Z"
    },
    "papermill": {
     "duration": 0.036028,
     "end_time": "2022-03-17T08:05:29.217983",
     "exception": false,
     "start_time": "2022-03-17T08:05:29.181955",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "93"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9c4a9cec",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:29.279369Z",
     "iopub.status.busy": "2022-03-17T08:05:29.278570Z",
     "iopub.status.idle": "2022-03-17T08:05:29.284583Z",
     "shell.execute_reply": "2022-03-17T08:05:29.285179Z",
     "shell.execute_reply.started": "2022-03-17T07:45:23.249484Z"
    },
    "papermill": {
     "duration": 0.038022,
     "end_time": "2022-03-17T08:05:29.285392",
     "exception": false,
     "start_time": "2022-03-17T08:05:29.247370",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7                           https://youtu.be/zBkVCpbNnkU\n",
       "119    Although I don't believe this to be true about...\n",
       "134    **”…the company knew there was asbestos in pro...\n",
       "145    Hi guys! I was wondering if you could help me ...\n",
       "161    Not sure if the sub allows this but I need to ...\n",
       "Name: body, dtype: object"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()['body']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "56ffec59",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:29.362214Z",
     "iopub.status.busy": "2022-03-17T08:05:29.361291Z",
     "iopub.status.idle": "2022-03-17T08:05:29.365751Z",
     "shell.execute_reply": "2022-03-17T08:05:29.365155Z",
     "shell.execute_reply.started": "2022-03-17T07:45:24.325367Z"
    },
    "papermill": {
     "duration": 0.050055,
     "end_time": "2022-03-17T08:05:29.365917",
     "exception": false,
     "start_time": "2022-03-17T08:05:29.315862",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>score</th>\n",
       "      <th>id</th>\n",
       "      <th>url</th>\n",
       "      <th>comms_num</th>\n",
       "      <th>created</th>\n",
       "      <th>body</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Fuck you anti-vaxxing retards</td>\n",
       "      <td>10</td>\n",
       "      <td>g6jkhp</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>8</td>\n",
       "      <td>1.587663e+09</td>\n",
       "      <td>https://youtu.be/zBkVCpbNnkU</td>\n",
       "      <td>2020-04-23 20:23:42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Is it biologically possible to insert a 5G tra...</td>\n",
       "      <td>9</td>\n",
       "      <td>khzpug</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>9</td>\n",
       "      <td>1.608647e+09</td>\n",
       "      <td>Although I don't believe this to be true about...</td>\n",
       "      <td>2020-12-22 16:19:39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>I don't see any reason to trust J&amp;J with a vac...</td>\n",
       "      <td>0</td>\n",
       "      <td>ocj9ws</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>4</td>\n",
       "      <td>1.625288e+09</td>\n",
       "      <td>**”…the company knew there was asbestos in pro...</td>\n",
       "      <td>2021-07-03 07:57:05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Vaccine Survey</td>\n",
       "      <td>0</td>\n",
       "      <td>ak5ziq</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>5</td>\n",
       "      <td>1.548543e+09</td>\n",
       "      <td>Hi guys! I was wondering if you could help me ...</td>\n",
       "      <td>2019-01-27 00:42:09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Can I have a rant please??</td>\n",
       "      <td>13</td>\n",
       "      <td>o6nqcm</td>\n",
       "      <td>https://www.reddit.com/r/VaccineMyths/comments...</td>\n",
       "      <td>1</td>\n",
       "      <td>1.624488e+09</td>\n",
       "      <td>Not sure if the sub allows this but I need to ...</td>\n",
       "      <td>2021-06-24 01:35:24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  score      id  \\\n",
       "0                      Fuck you anti-vaxxing retards     10  g6jkhp   \n",
       "1  Is it biologically possible to insert a 5G tra...      9  khzpug   \n",
       "2  I don't see any reason to trust J&J with a vac...      0  ocj9ws   \n",
       "3                                     Vaccine Survey      0  ak5ziq   \n",
       "4                         Can I have a rant please??     13  o6nqcm   \n",
       "\n",
       "                                                 url  comms_num       created  \\\n",
       "0  https://www.reddit.com/r/VaccineMyths/comments...          8  1.587663e+09   \n",
       "1  https://www.reddit.com/r/VaccineMyths/comments...          9  1.608647e+09   \n",
       "2  https://www.reddit.com/r/VaccineMyths/comments...          4  1.625288e+09   \n",
       "3  https://www.reddit.com/r/VaccineMyths/comments...          5  1.548543e+09   \n",
       "4  https://www.reddit.com/r/VaccineMyths/comments...          1  1.624488e+09   \n",
       "\n",
       "                                                body            timestamp  \n",
       "0                       https://youtu.be/zBkVCpbNnkU  2020-04-23 20:23:42  \n",
       "1  Although I don't believe this to be true about...  2020-12-22 16:19:39  \n",
       "2  **”…the company knew there was asbestos in pro...  2021-07-03 07:57:05  \n",
       "3  Hi guys! I was wondering if you could help me ...  2019-01-27 00:42:09  \n",
       "4  Not sure if the sub allows this but I need to ...  2021-06-24 01:35:24  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.reset_index(drop=True)\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0f054888",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:29.434102Z",
     "iopub.status.busy": "2022-03-17T08:05:29.433283Z",
     "iopub.status.idle": "2022-03-17T08:05:31.437321Z",
     "shell.execute_reply": "2022-03-17T08:05:31.436709Z",
     "shell.execute_reply.started": "2022-03-17T07:46:55.189690Z"
    },
    "papermill": {
     "duration": 2.04158,
     "end_time": "2022-03-17T08:05:31.437539",
     "exception": false,
     "start_time": "2022-03-17T08:05:29.395959",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from nltk.tokenize.casual import casual_tokenize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "55a5ec1d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:31.499989Z",
     "iopub.status.busy": "2022-03-17T08:05:31.499162Z",
     "iopub.status.idle": "2022-03-17T08:05:31.613787Z",
     "shell.execute_reply": "2022-03-17T08:05:31.613115Z",
     "shell.execute_reply.started": "2022-03-17T07:48:57.797897Z"
    },
    "papermill": {
     "duration": 0.14705,
     "end_time": "2022-03-17T08:05:31.613972",
     "exception": false,
     "start_time": "2022-03-17T08:05:31.466922",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "tfidf = TfidfVectorizer(tokenizer=casual_tokenize)\n",
    "tfidf_docs = tfidf.fit_transform(df.body).toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "767c878e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:31.679733Z",
     "iopub.status.busy": "2022-03-17T08:05:31.679001Z",
     "iopub.status.idle": "2022-03-17T08:05:31.684859Z",
     "shell.execute_reply": "2022-03-17T08:05:31.684162Z",
     "shell.execute_reply.started": "2022-03-17T07:49:04.795668Z"
    },
    "papermill": {
     "duration": 0.040223,
     "end_time": "2022-03-17T08:05:31.685016",
     "exception": false,
     "start_time": "2022-03-17T08:05:31.644793",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "93"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tfidf_docs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4db8fc3f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:31.749502Z",
     "iopub.status.busy": "2022-03-17T08:05:31.748421Z",
     "iopub.status.idle": "2022-03-17T08:05:31.755822Z",
     "shell.execute_reply": "2022-03-17T08:05:31.756416Z",
     "shell.execute_reply.started": "2022-03-17T07:49:59.287829Z"
    },
    "papermill": {
     "duration": 0.041973,
     "end_time": "2022-03-17T08:05:31.756643",
     "exception": false,
     "start_time": "2022-03-17T08:05:31.714670",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       ...,\n",
       "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       [0.        , 0.10318017, 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ],\n",
       "       [0.08889355, 0.        , 0.        , ..., 0.        , 0.        ,\n",
       "        0.        ]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tfidf_docs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "21361802",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:31.821582Z",
     "iopub.status.busy": "2022-03-17T08:05:31.820588Z",
     "iopub.status.idle": "2022-03-17T08:05:31.826832Z",
     "shell.execute_reply": "2022-03-17T08:05:31.827286Z",
     "shell.execute_reply.started": "2022-03-17T07:51:00.915175Z"
    },
    "papermill": {
     "duration": 0.040611,
     "end_time": "2022-03-17T08:05:31.827502",
     "exception": false,
     "start_time": "2022-03-17T08:05:31.786891",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(93, 2928)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tfidf_docs.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1ca73b4b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:31.896732Z",
     "iopub.status.busy": "2022-03-17T08:05:31.895829Z",
     "iopub.status.idle": "2022-03-17T08:05:31.899382Z",
     "shell.execute_reply": "2022-03-17T08:05:31.899893Z",
     "shell.execute_reply.started": "2022-03-17T07:51:40.045601Z"
    },
    "papermill": {
     "duration": 0.041949,
     "end_time": "2022-03-17T08:05:31.900090",
     "exception": false,
     "start_time": "2022-03-17T08:05:31.858141",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2928"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tfidf.vocabulary_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "79fd153a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:31.967042Z",
     "iopub.status.busy": "2022-03-17T08:05:31.966017Z",
     "iopub.status.idle": "2022-03-17T08:05:31.997503Z",
     "shell.execute_reply": "2022-03-17T08:05:31.998054Z",
     "shell.execute_reply.started": "2022-03-17T07:54:16.306414Z"
    },
    "papermill": {
     "duration": 0.066578,
     "end_time": "2022-03-17T08:05:31.998274",
     "exception": false,
     "start_time": "2022-03-17T08:05:31.931696",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>...</th>\n",
       "      <th>2918</th>\n",
       "      <th>2919</th>\n",
       "      <th>2920</th>\n",
       "      <th>2921</th>\n",
       "      <th>2922</th>\n",
       "      <th>2923</th>\n",
       "      <th>2924</th>\n",
       "      <th>2925</th>\n",
       "      <th>2926</th>\n",
       "      <th>2927</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.031168</td>\n",
       "      <td>0.062336</td>\n",
       "      <td>0.046647</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.208562</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.020552</td>\n",
       "      <td>0.277257</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 2928 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       0         1     2     3     4     5     6     7     8     9     ...  \\\n",
       "0  0.000000  0.000000   0.0   0.0   0.0   0.0   0.0   0.0   0.0   0.0  ...   \n",
       "1  0.000000  0.000000   0.0   0.0   0.0   0.0   0.0   0.0   0.0   0.0  ...   \n",
       "2  0.000000  0.000000   0.0   0.0   0.0   0.0   0.0   0.0   0.0   0.0  ...   \n",
       "3  0.208562  0.000000   0.0   0.0   0.0   0.0   0.0   0.0   0.0   0.0  ...   \n",
       "4  0.020552  0.277257   0.0   0.0   0.0   0.0   0.0   0.0   0.0   0.0  ...   \n",
       "\n",
       "   2918  2919  2920      2921      2922      2923  2924  2925  2926  2927  \n",
       "0   0.0   0.0   0.0  0.000000  0.000000  0.000000   0.0   0.0   0.0   0.0  \n",
       "1   0.0   0.0   0.0  0.000000  0.000000  0.000000   0.0   0.0   0.0   0.0  \n",
       "2   0.0   0.0   0.0  0.031168  0.062336  0.046647   0.0   0.0   0.0   0.0  \n",
       "3   0.0   0.0   0.0  0.000000  0.000000  0.000000   0.0   0.0   0.0   0.0  \n",
       "4   0.0   0.0   0.0  0.000000  0.000000  0.000000   0.0   0.0   0.0   0.0  \n",
       "\n",
       "[5 rows x 2928 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tfidf_docs = pd.DataFrame(tfidf_docs)\n",
    "tfidf_docs.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "72e0987a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:32.066544Z",
     "iopub.status.busy": "2022-03-17T08:05:32.065545Z",
     "iopub.status.idle": "2022-03-17T08:05:32.085119Z",
     "shell.execute_reply": "2022-03-17T08:05:32.085669Z",
     "shell.execute_reply.started": "2022-03-17T07:56:20.024725Z"
    },
    "papermill": {
     "duration": 0.056181,
     "end_time": "2022-03-17T08:05:32.085880",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.029699",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "tfidf_docs = tfidf_docs - tfidf_docs.mean() # centers the BOW vectors by subtracting the mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b2480501",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:32.154144Z",
     "iopub.status.busy": "2022-03-17T08:05:32.153155Z",
     "iopub.status.idle": "2022-03-17T08:05:32.178218Z",
     "shell.execute_reply": "2022-03-17T08:05:32.178901Z",
     "shell.execute_reply.started": "2022-03-17T07:56:30.561160Z"
    },
    "papermill": {
     "duration": 0.061547,
     "end_time": "2022-03-17T08:05:32.179099",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.117552",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>...</th>\n",
       "      <th>2918</th>\n",
       "      <th>2919</th>\n",
       "      <th>2920</th>\n",
       "      <th>2921</th>\n",
       "      <th>2922</th>\n",
       "      <th>2923</th>\n",
       "      <th>2924</th>\n",
       "      <th>2925</th>\n",
       "      <th>2926</th>\n",
       "      <th>2927</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-0.027184</td>\n",
       "      <td>-0.032985</td>\n",
       "      <td>-0.001743</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.000805</td>\n",
       "      <td>-0.004825</td>\n",
       "      <td>-0.044789</td>\n",
       "      <td>-0.004989</td>\n",
       "      <td>-0.005324</td>\n",
       "      <td>-0.000502</td>\n",
       "      <td>-0.000111</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.003212</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-0.027184</td>\n",
       "      <td>-0.032985</td>\n",
       "      <td>-0.001743</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.000805</td>\n",
       "      <td>-0.004825</td>\n",
       "      <td>-0.044789</td>\n",
       "      <td>-0.004989</td>\n",
       "      <td>-0.005324</td>\n",
       "      <td>-0.000502</td>\n",
       "      <td>-0.000111</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.003212</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-0.027184</td>\n",
       "      <td>-0.032985</td>\n",
       "      <td>-0.001743</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.000805</td>\n",
       "      <td>-0.004825</td>\n",
       "      <td>-0.044789</td>\n",
       "      <td>0.026179</td>\n",
       "      <td>0.057012</td>\n",
       "      <td>0.046145</td>\n",
       "      <td>-0.000111</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.003212</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.181378</td>\n",
       "      <td>-0.032985</td>\n",
       "      <td>-0.001743</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.000805</td>\n",
       "      <td>-0.004825</td>\n",
       "      <td>-0.044789</td>\n",
       "      <td>-0.004989</td>\n",
       "      <td>-0.005324</td>\n",
       "      <td>-0.000502</td>\n",
       "      <td>-0.000111</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.003212</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-0.006632</td>\n",
       "      <td>0.244273</td>\n",
       "      <td>-0.001743</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>-0.001243</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.000805</td>\n",
       "      <td>-0.004825</td>\n",
       "      <td>-0.044789</td>\n",
       "      <td>-0.004989</td>\n",
       "      <td>-0.005324</td>\n",
       "      <td>-0.000502</td>\n",
       "      <td>-0.000111</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.006424</td>\n",
       "      <td>-0.003212</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 2928 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       0         1         2         3         4         5         6     \\\n",
       "0 -0.027184 -0.032985 -0.001743 -0.001243 -0.001243 -0.001243 -0.001243   \n",
       "1 -0.027184 -0.032985 -0.001743 -0.001243 -0.001243 -0.001243 -0.001243   \n",
       "2 -0.027184 -0.032985 -0.001743 -0.001243 -0.001243 -0.001243 -0.001243   \n",
       "3  0.181378 -0.032985 -0.001743 -0.001243 -0.001243 -0.001243 -0.001243   \n",
       "4 -0.006632  0.244273 -0.001743 -0.001243 -0.001243 -0.001243 -0.001243   \n",
       "\n",
       "       7         8         9     ...      2918      2919      2920      2921  \\\n",
       "0 -0.001243 -0.001243 -0.001243  ... -0.000805 -0.004825 -0.044789 -0.004989   \n",
       "1 -0.001243 -0.001243 -0.001243  ... -0.000805 -0.004825 -0.044789 -0.004989   \n",
       "2 -0.001243 -0.001243 -0.001243  ... -0.000805 -0.004825 -0.044789  0.026179   \n",
       "3 -0.001243 -0.001243 -0.001243  ... -0.000805 -0.004825 -0.044789 -0.004989   \n",
       "4 -0.001243 -0.001243 -0.001243  ... -0.000805 -0.004825 -0.044789 -0.004989   \n",
       "\n",
       "       2922      2923      2924      2925      2926      2927  \n",
       "0 -0.005324 -0.000502 -0.000111 -0.006424 -0.006424 -0.003212  \n",
       "1 -0.005324 -0.000502 -0.000111 -0.006424 -0.006424 -0.003212  \n",
       "2  0.057012  0.046145 -0.000111 -0.006424 -0.006424 -0.003212  \n",
       "3 -0.005324 -0.000502 -0.000111 -0.006424 -0.006424 -0.003212  \n",
       "4 -0.005324 -0.000502 -0.000111 -0.006424 -0.006424 -0.003212  \n",
       "\n",
       "[5 rows x 2928 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tfidf_docs.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9879604e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:32.247743Z",
     "iopub.status.busy": "2022-03-17T08:05:32.246716Z",
     "iopub.status.idle": "2022-03-17T08:05:32.252742Z",
     "shell.execute_reply": "2022-03-17T08:05:32.253341Z",
     "shell.execute_reply.started": "2022-03-17T07:57:04.205603Z"
    },
    "papermill": {
     "duration": 0.042226,
     "end_time": "2022-03-17T08:05:32.253554",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.211328",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(93, 2928)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tfidf_docs.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1abf31c",
   "metadata": {
    "papermill": {
     "duration": 0.032477,
     "end_time": "2022-03-17T08:05:32.318708",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.286231",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Semantic Analysis using PCA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7def12c7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:32.390681Z",
     "iopub.status.busy": "2022-03-17T08:05:32.389387Z",
     "iopub.status.idle": "2022-03-17T08:05:32.426723Z",
     "shell.execute_reply": "2022-03-17T08:05:32.427238Z",
     "shell.execute_reply.started": "2022-03-17T07:59:21.759917Z"
    },
    "papermill": {
     "duration": 0.076369,
     "end_time": "2022-03-17T08:05:32.427497",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.351128",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.decomposition import PCA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "85fc5d87",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:32.497438Z",
     "iopub.status.busy": "2022-03-17T08:05:32.496731Z",
     "iopub.status.idle": "2022-03-17T08:05:32.719777Z",
     "shell.execute_reply": "2022-03-17T08:05:32.720686Z",
     "shell.execute_reply.started": "2022-03-17T08:01:27.329749Z"
    },
    "papermill": {
     "duration": 0.26011,
     "end_time": "2022-03-17T08:05:32.721008",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.460898",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "pca = PCA(n_components=8)\n",
    "pca = pca.fit(tfidf_docs)\n",
    "pca_topic_vectors = pca.transform(tfidf_docs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5573b633",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:32.845318Z",
     "iopub.status.busy": "2022-03-17T08:05:32.844671Z",
     "iopub.status.idle": "2022-03-17T08:05:32.847656Z",
     "shell.execute_reply": "2022-03-17T08:05:32.847092Z",
     "shell.execute_reply.started": "2022-03-17T08:02:07.437932Z"
    },
    "papermill": {
     "duration": 0.067423,
     "end_time": "2022-03-17T08:05:32.847819",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.780396",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "columns = ['topic{}'.format(i) for i in range(pca.n_components)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1630bc14",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-17T08:05:32.933107Z",
     "iopub.status.busy": "2022-03-17T08:05:32.932374Z",
     "iopub.status.idle": "2022-03-17T08:05:32.936810Z",
     "shell.execute_reply": "2022-03-17T08:05:32.937341Z",
     "shell.execute_reply.started": "2022-03-17T08:03:35.749668Z"
    },
    "papermill": {
     "duration": 0.057353,
     "end_time": "2022-03-17T08:05:32.937559",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.880206",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>topic0</th>\n",
       "      <th>topic1</th>\n",
       "      <th>topic2</th>\n",
       "      <th>topic3</th>\n",
       "      <th>topic4</th>\n",
       "      <th>topic5</th>\n",
       "      <th>topic6</th>\n",
       "      <th>topic7</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.331</td>\n",
       "      <td>0.059</td>\n",
       "      <td>-0.015</td>\n",
       "      <td>-0.024</td>\n",
       "      <td>-0.046</td>\n",
       "      <td>-0.083</td>\n",
       "      <td>-0.078</td>\n",
       "      <td>0.156</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.068</td>\n",
       "      <td>0.064</td>\n",
       "      <td>-0.056</td>\n",
       "      <td>-0.093</td>\n",
       "      <td>-0.098</td>\n",
       "      <td>-0.151</td>\n",
       "      <td>-0.102</td>\n",
       "      <td>-0.143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.246</td>\n",
       "      <td>-0.173</td>\n",
       "      <td>0.710</td>\n",
       "      <td>-0.309</td>\n",
       "      <td>-0.066</td>\n",
       "      <td>0.092</td>\n",
       "      <td>0.019</td>\n",
       "      <td>-0.035</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.162</td>\n",
       "      <td>0.086</td>\n",
       "      <td>-0.041</td>\n",
       "      <td>0.167</td>\n",
       "      <td>-0.285</td>\n",
       "      <td>-0.006</td>\n",
       "      <td>0.272</td>\n",
       "      <td>-0.172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-0.299</td>\n",
       "      <td>-0.035</td>\n",
       "      <td>-0.113</td>\n",
       "      <td>-0.092</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.033</td>\n",
       "      <td>0.097</td>\n",
       "      <td>-0.068</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>-0.242</td>\n",
       "      <td>0.004</td>\n",
       "      <td>-0.111</td>\n",
       "      <td>-0.119</td>\n",
       "      <td>0.009</td>\n",
       "      <td>0.072</td>\n",
       "      <td>0.066</td>\n",
       "      <td>0.020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0.039</td>\n",
       "      <td>0.005</td>\n",
       "      <td>0.272</td>\n",
       "      <td>-0.219</td>\n",
       "      <td>-0.132</td>\n",
       "      <td>-0.092</td>\n",
       "      <td>0.163</td>\n",
       "      <td>-0.164</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>-0.297</td>\n",
       "      <td>0.335</td>\n",
       "      <td>0.107</td>\n",
       "      <td>0.105</td>\n",
       "      <td>0.020</td>\n",
       "      <td>0.076</td>\n",
       "      <td>-0.242</td>\n",
       "      <td>-0.202</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   topic0  topic1  topic2  topic3  topic4  topic5  topic6  topic7\n",
       "0   0.331   0.059  -0.015  -0.024  -0.046  -0.083  -0.078   0.156\n",
       "1   0.068   0.064  -0.056  -0.093  -0.098  -0.151  -0.102  -0.143\n",
       "2   0.246  -0.173   0.710  -0.309  -0.066   0.092   0.019  -0.035\n",
       "3   0.162   0.086  -0.041   0.167  -0.285  -0.006   0.272  -0.172\n",
       "4  -0.299  -0.035  -0.113  -0.092   0.001  -0.033   0.097  -0.068\n",
       "5  -0.242   0.004  -0.111  -0.119   0.009   0.072   0.066   0.020\n",
       "6   0.039   0.005   0.272  -0.219  -0.132  -0.092   0.163  -0.164\n",
       "7  -0.297   0.335   0.107   0.105   0.020   0.076  -0.242  -0.202"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pca_topic_vectors = pd.DataFrame(pca_topic_vectors, columns=columns)\n",
    "pca_topic_vectors.round(3).head(8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "299cb465",
   "metadata": {
    "papermill": {
     "duration": 0.03305,
     "end_time": "2022-03-17T08:05:33.004166",
     "exception": false,
     "start_time": "2022-03-17T08:05:32.971116",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 16.653477,
   "end_time": "2022-03-17T08:05:33.853327",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-03-17T08:05:17.199850",
   "version": "2.3.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
