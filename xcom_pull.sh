echo "hello pull started"
echo '{{ ti.xcom_pull(KEY06) }}'
echo "{{ ti.xcom_pull(KEY07) }}"
echo '{{ ti.xcom_pull(task_ids="s1",key="KEY08") }}'
echo "{{ ti.xcom_pull(task_ids='s1',key='NEERAJ') }}"
echo "Pull ended"
