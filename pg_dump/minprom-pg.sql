PGDMP         6            	    {         
   minprom-tg    13.5    13.2 %    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    1236030 
   minprom-tg    DATABASE     i   CREATE DATABASE "minprom-tg" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "minprom-tg";
                postgres    false                        2615    1236036    content    SCHEMA        CREATE SCHEMA content;
    DROP SCHEMA content;
                postgres    false            �            1259    1236085    appeal    TABLE     �   CREATE TABLE content.appeal (
    text character varying NOT NULL,
    user_id uuid,
    id uuid NOT NULL,
    creation_date timestamp without time zone
);
    DROP TABLE content.appeal;
       content         heap    postgres    false    4            �            1259    1260607    link    TABLE     �   CREATE TABLE content.link (
    url character varying NOT NULL,
    name character varying(100) NOT NULL,
    "order" character varying NOT NULL,
    id uuid NOT NULL,
    creation_date timestamp without time zone
);
    DROP TABLE content.link;
       content         heap    postgres    false    4            �            1259    1236037    role    TABLE     �   CREATE TABLE content.role (
    name character varying NOT NULL,
    id uuid NOT NULL,
    creation_date timestamp without time zone
);
    DROP TABLE content.role;
       content         heap    postgres    false    4            �            1259    1236077    text_message    TABLE     �   CREATE TABLE content.text_message (
    text character varying NOT NULL,
    name character varying(50) NOT NULL,
    id uuid NOT NULL,
    creation_date timestamp without time zone
);
 !   DROP TABLE content.text_message;
       content         heap    postgres    false    4            �            1259    1236047    user    TABLE     7  CREATE TABLE content."user" (
    telegram_id bigint NOT NULL,
    telegram_username character varying,
    telegram_first_name character varying,
    telegram_last_name character varying,
    telegram_full_name character varying NOT NULL,
    id uuid NOT NULL,
    creation_date timestamp without time zone
);
    DROP TABLE content."user";
       content         heap    postgres    false    4            �            1259    1236059 	   user_role    TABLE     q   CREATE TABLE content.user_role (
    id bigint NOT NULL,
    user_id uuid NOT NULL,
    role_id uuid NOT NULL
);
    DROP TABLE content.user_role;
       content         heap    postgres    false    4            �            1259    1236057    user_role_id_seq    SEQUENCE     z   CREATE SEQUENCE content.user_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE content.user_role_id_seq;
       content          postgres    false    205    4            �           0    0    user_role_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE content.user_role_id_seq OWNED BY content.user_role.id;
          content          postgres    false    204            �            1259    1236031    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            @           2604    1236062    user_role id    DEFAULT     n   ALTER TABLE ONLY content.user_role ALTER COLUMN id SET DEFAULT nextval('content.user_role_id_seq'::regclass);
 <   ALTER TABLE content.user_role ALTER COLUMN id DROP DEFAULT;
       content          postgres    false    204    205    205            �          0    1236085    appeal 
   TABLE DATA           C   COPY content.appeal (text, user_id, id, creation_date) FROM stdin;
    content          postgres    false    207   j)       �          0    1260607    link 
   TABLE DATA           F   COPY content.link (url, name, "order", id, creation_date) FROM stdin;
    content          postgres    false    208   �)       �          0    1236037    role 
   TABLE DATA           8   COPY content.role (name, id, creation_date) FROM stdin;
    content          postgres    false    202   9.       �          0    1236077    text_message 
   TABLE DATA           F   COPY content.text_message (text, name, id, creation_date) FROM stdin;
    content          postgres    false    206   �.       �          0    1236047    user 
   TABLE DATA           �   COPY content."user" (telegram_id, telegram_username, telegram_first_name, telegram_last_name, telegram_full_name, id, creation_date) FROM stdin;
    content          postgres    false    203   E7       �          0    1236059 	   user_role 
   TABLE DATA           :   COPY content.user_role (id, user_id, role_id) FROM stdin;
    content          postgres    false    205   b7       �          0    1236031    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    201   7       �           0    0    user_role_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('content.user_role_id_seq', 1, false);
          content          postgres    false    204            R           2606    1236092    appeal appeal_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY content.appeal
    ADD CONSTRAINT appeal_pkey PRIMARY KEY (id);
 =   ALTER TABLE ONLY content.appeal DROP CONSTRAINT appeal_pkey;
       content            postgres    false    207            T           2606    1260616    link link_order_key 
   CONSTRAINT     R   ALTER TABLE ONLY content.link
    ADD CONSTRAINT link_order_key UNIQUE ("order");
 >   ALTER TABLE ONLY content.link DROP CONSTRAINT link_order_key;
       content            postgres    false    208            V           2606    1260614    link link_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY content.link
    ADD CONSTRAINT link_pkey PRIMARY KEY (id);
 9   ALTER TABLE ONLY content.link DROP CONSTRAINT link_pkey;
       content            postgres    false    208            D           2606    1236046    role role_name_key 
   CONSTRAINT     N   ALTER TABLE ONLY content.role
    ADD CONSTRAINT role_name_key UNIQUE (name);
 =   ALTER TABLE ONLY content.role DROP CONSTRAINT role_name_key;
       content            postgres    false    202            F           2606    1236044    role role_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY content.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id);
 9   ALTER TABLE ONLY content.role DROP CONSTRAINT role_pkey;
       content            postgres    false    202            P           2606    1236084    text_message text_message_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY content.text_message
    ADD CONSTRAINT text_message_pkey PRIMARY KEY (id);
 I   ALTER TABLE ONLY content.text_message DROP CONSTRAINT text_message_pkey;
       content            postgres    false    206            H           2606    1236054    user user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY content."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 ;   ALTER TABLE ONLY content."user" DROP CONSTRAINT user_pkey;
       content            postgres    false    203            L           2606    1236066    user_role user_role_id_key 
   CONSTRAINT     T   ALTER TABLE ONLY content.user_role
    ADD CONSTRAINT user_role_id_key UNIQUE (id);
 E   ALTER TABLE ONLY content.user_role DROP CONSTRAINT user_role_id_key;
       content            postgres    false    205            N           2606    1236064    user_role user_role_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY content.user_role
    ADD CONSTRAINT user_role_pkey PRIMARY KEY (id, user_id, role_id);
 C   ALTER TABLE ONLY content.user_role DROP CONSTRAINT user_role_pkey;
       content            postgres    false    205    205    205            J           2606    1236056    user user_telegram_id_key 
   CONSTRAINT     ^   ALTER TABLE ONLY content."user"
    ADD CONSTRAINT user_telegram_id_key UNIQUE (telegram_id);
 F   ALTER TABLE ONLY content."user" DROP CONSTRAINT user_telegram_id_key;
       content            postgres    false    203            B           2606    1236035 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    201            Y           2606    1236093    appeal appeal_user_id_fkey    FK CONSTRAINT     |   ALTER TABLE ONLY content.appeal
    ADD CONSTRAINT appeal_user_id_fkey FOREIGN KEY (user_id) REFERENCES content."user"(id);
 E   ALTER TABLE ONLY content.appeal DROP CONSTRAINT appeal_user_id_fkey;
       content          postgres    false    203    2888    207            W           2606    1236067     user_role user_role_role_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY content.user_role
    ADD CONSTRAINT user_role_role_id_fkey FOREIGN KEY (role_id) REFERENCES content.role(id);
 K   ALTER TABLE ONLY content.user_role DROP CONSTRAINT user_role_role_id_fkey;
       content          postgres    false    2886    205    202            X           2606    1236072     user_role user_role_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY content.user_role
    ADD CONSTRAINT user_role_user_id_fkey FOREIGN KEY (user_id) REFERENCES content."user"(id);
 K   ALTER TABLE ONLY content.user_role DROP CONSTRAINT user_role_user_id_fkey;
       content          postgres    false    203    2888    205            �      x������ � �      �   �  x���[OG���_�?0xvw��(�q�18UBsZ� �M8]%�9TT�M���i��Vr	+��/���~�8($.��ʖ�;���y��{gj;;[��lV�;���)��x�IVd׊�p�`6���Ԥ��T}�O�;�<R����Թ�������i�\���Յ�{�5�o��s]d;>E����H�B��;���-��A�$؟p�陶��FֳmT���w�����3�Ϫd]u��2j ���H4�z�Q���pwW�%��5��\��@��aq]cݰ� &�[����!���ȕ�m
���ٹZ3��,u�j�V��m�������3�����Ї9XVO�aY0?����9��9|;6�!¤K���j`91&L��G�HU�U�u���Hi2$P����c��B�Bkyl���:f ���ԓF����f���V��J�]�7�4yj�į����0��v��\Eu�I��;]��x���0�=�L��a��7�GS�C6J W�4)�K���8*��V�M��_��aۉ{��0���xo>�/4抛�'�;m�Ġ�׶ж��L��U����i0�&�>
9����"&	E%D��OR�����J��Q!�&>�G�!JD����~�z���}b-��<X�*>j����Lmr$퇠�i��a��zD+b�P����:iN��.��=�$�u��Nn�5��,`��mKr�CE��� ߖ ���>桃Sa�Kny���K�B~0I��^��F��G�F��IH��]$I^�����l°�m'Syy�^.��ť��bu�t(m4��tZ�-�����B7�:�p�<�΁d<"ϳ}fq���w�]���<@����l������#���X���!�q	l�\p�c� S����T]>Ӛ_۪V�9L�P��� Q�R3�/�`׍�a8�sL�x��G��&�=�!��(�r�J��\{�q0]�� {� �ۤ�}]����"cӐ�7��b�5#P8j��"�w-�.�;[s����PwwfG:lX��^R�����A�2,�s�3�" ������y��$]��-�4��WO6�9���X���}���~$��b���ͪ٩�X����>S���[�Gdl��o�����f���Jet˞$�O&�j%R�-d{��ֿ �f|ll�o�bQ�      �   L   x���� �3��J���Y�@�ă���y�ϗ��W��\uO��m���U����j0 �XV�����~�,,      �   �  x��Y�n�V}���}( :�ԇ��_�۠h��g�c9��$c��`0(:�(@�bLK����/龜CR�䤹�	,�<<{��׾�M��\�����̊S��	�XO��e�=�xj�;���=�?�kX�rQ��Wt!+�25d&7�.��iqV\��Vʤ8�=�3���b�Ko{����:�'�'����q��ig��a��B��Dx��X�&�'f���p�پ�q,��@8�a��?��Fn���+p+T��?���������Ӓ{����N|��x��ߦ���G��E<��g;��@x;���9�:��>��[� ��+��
4��{�v^ �2�� ~wS�8G!�%� %h)Ė˻�E�\��|�����U�%�Q.e��*�芼3�r�b�	ҵ�\!��1�^�e�v��G�JbN@�������(`���le8rl-7I��G�3�����)�C�l�L�K=�+ݣ�L;��d��������4����P�/f���q4�&v���е�aF��@rH�KW�U��1��������� w�!W��3��ʗK�Q�,�Pf�h� f}u�ڼW���@�9m�#0$1}/�QkzHGtJ��@>Cc�/��G�ɞA`p�=S7>�0����V��pZ�&�3rz��Q<!��g�G���R_K�g���h3$m0�Oi2��~φj���M�9�Ej	:]��$�,F��`�s��5|<��V	"���Q�W3>�~,�@Bd���2�^��RF���{����lat�*�2&>u�u7�g�	b�-ˠGhy���8N(E\S�>#�:�u��5�5� ��3&�%$,��K9U��Ƈl��0H옰�5�-251sy���P0�a�"�I�[=���Tc~ؙ��>��}�����Z�)��H�eu�.�Fq��𵪺7�o)&�c�H���+Z��Y�(j�g�.[E��
	]�r7$:'Z���P�FW��b���*條d��g��deZ��ܑ�0nC�:`�gA�V��?�s
�%�:CK��n�
������\B��u�,^�@��yy��J�O*KoאA��-�jNҞt��0���N;C�����F�m]�sJ�d7�E{���r#����T+�6a�%ˌ��p�����oF���}�5��)��X��lE7�$*�<B ��=b&�bY�.�4�M��V�p�у��Cca1|T�s�p}�Ծj��噥�k% ��4��7r�r�.��U)���~�ŵ��?��!�l�ܪH;;���
sV-�/8�e|�x��T%�5y��H���k�1�����+pą��u���KT~�f�T���+�i������۩��6�V}Rbڙor�=��x������@[��֢It�/���$�p�(�x^A�b��w��ȹbݨ��d��j�ܚ-6���_8oz%�w47��1���<Y��nW�1�~�IZQO9�C�J�\T��-��"�G#��M1�Շ!!'�+J�p���f�h��#�� �KA�D5b��<9P�R�;��fk�����͇�%�q>��a�P���1]ֶq���ڶM�k��S]C_�)oUZ�Kչ�X�<�#+�����u���o���GHLX�	B�S��|wq�şv�RW��N)�Ìץ��F	-��p������)F�[�Ӌ'�L�{H�J��9��H�k*�OX���f/7/��z��!�<�,`[�]*t�=C��u6�*�uHB��G�q�v%��P�+��\ye�<5�C�3M��z��ڠ����2ϼR�3ǖһ4ɨ�eחm�3���+o�0W*�V\T��G]���:�;��v1��7�~�P�������	r��L�p[b�eV��+E��#�K���;��/���ƹC���1y�>0�@1K]����~g�h�ׯ�G'�⋣٣���ƞ�_x�e�ز"a{�4�'t��K
�ZQ��Љ�+5Y���{!�S���Ű���/�O:�h��,�ؙ	/��`d�pfO�IL|�mb���ﻖ �G�����9r�+�wx��=1_`ت������]��7����5�,ϟ�b�,�O��}ažc�C+t�q�����g���v@���=�w�7\�>ّ�>��WR(�q4��q$F� 
��z�	�`��$�l�ɴ�a������~xp�?88�«oe      �      x������ � �      �      x������ � �      �      x�33HLIJIM��H2����� 2#u     